from collections import OrderedDict
from inspect import signature, Parameter
from itertools import chain


def curry(func, *args, **kwargs):
    # Cannot curry an already curried function since our __call__ has *args
    # and **kwargs, which violates our currying rules.
    if isinstance(func, _curry):
        # Since curry objects are immutable, we can return the same curry
        return func

    params = signature(func).parameters

    if any(_is_star_param(param) for param in params.values()):
        raise TypeError('cannot curry a function with *args or **kwargs')

    if any(param.default != Parameter.empty for param in params.values()):
        raise TypeError('cannot curry a function with default arguments')

    curried = _curry(func, params, (), OrderedDict())

    if args or kwargs:
        return curried(*args, **kwargs)

    return curried


class _curry:
    def __init__(self, func, remaining_params, args, kwargs):
        self._func = func
        self._remaining_params = remaining_params
        self._args = args
        self._kwargs = kwargs

    def __call__(self, *args, **kwargs):
        if not args and not kwargs:
            return self

        if self._kwargs and args:
            raise SyntaxError('positional argument follows keyword argument')

        # Ensure we haven't been passed too many positional arguments
        remaining_params_iter = iter(self._remaining_params.items())

        try:
            for _, (_, expected) in _zip_first(args, remaining_params_iter):
                if not _is_positional_param(expected):
                    raise self._positional_error(len(args))
        except ShortIteratorError:
            raise self._positional_error(len(args))

        # _zip_first will have consumed all of the positional arguments passed.
        # What remains is the positional and keyword argument that haven't been
        # provided.
        new_remaining_params = OrderedDict(remaining_params_iter)

        # Ensure all passed keyword arguments are expected (and eliminate all
        # remaining parameters that are passed)
        for name in kwargs:
            try:
                del new_remaining_params[name]
            except KeyError:
                raise self._type_error(f'got an unexpected keyword argument '
                                       f'\'{name}\'')

        # If all arguments have been provided, call then function
        new_args = self._args + args
        new_kwargs = OrderedDict(chain(self._kwargs.items(), kwargs.items()))

        if not new_remaining_params:
            return self._func(*new_args, **new_kwargs)

        # Otherwise, add the new arguments and return a new curryable function
        return self.__class__(self._func, new_remaining_params, new_args,
                              new_kwargs)

    def _positional_error(self, extra_given):
        remaining_positional = filter(_is_positional_param,
                                      self._remaining_params.values())
        expected = len(self._args) + len(list(remaining_positional))
        s = 's' if expected != 1 else ''

        given = len(self._args) + extra_given

        return self._type_error(f'takes {expected} positional argument{s} but '
                                f'{given} were given')

    def _type_error(self, msg):
        return TypeError(f'{self._func.__name__}() {msg}')


def _is_star_param(param):
    return param.kind in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD)


def _is_positional_param(param):
    return param.kind in (Parameter.POSITIONAL_ONLY,
                          Parameter.POSITIONAL_OR_KEYWORD)


def _zip_first(first, *rest):
    first = iter(first)
    rest = tuple(map(iter, rest))

    for item in first:
        other_items = tuple(map(next, rest))
        if len(other_items) != len(rest):
            raise ShortIteratorError()

        yield (item, *other_items)


class ShortIteratorError(Exception):
    def __init__(self):
        super().__init__('iterator unexpectedly stopped')
