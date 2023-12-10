



Day 11 - Advent of Code 2023



window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


# [Advent of Code](/)

* [[About]](/2023/about)
* [[Events]](/2023/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Settings]](/2023/settings)
* [[Log Out]](/2023/auth/logout)
weiss-i-net 20\*#   {:year [2023](/2023)}

* [[Calendar]](/2023)
* [[AoC++]](/2023/support)
* [[Sponsors]](/2023/sponsors)
* [[Leaderboard]](/2023/leaderboard)
* [[Stats]](/2023/stats)


Our [sponsors](/2023/sponsors) help make Advent of Code possible:[Boot.dev](https://www.boot.dev?promo=ADVENTOFCODE) - Ready to become a backend developer? If you like AoC, you might be like us. We think smartest way to learn to code is to ensure you're never bored. Try the most captivating, addictive way to learn to code on Boot.dev.


## --- Day 11: Cosmic Expansion ---

You continue following signs for "Hot Springs" and eventually come across an [observatory](https://en.wikipedia.org/wiki/Observatory). The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.


He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.


Maybe you can help him with the analysis to speed things up?


The researcher has collected a bunch of data and compiled the data into a single giant *image* (your puzzle input). The image includes *empty space* (`.`) and *galaxies* (`#`). For example:



```
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....

```

The researcher is trying to figure out the sum of the lengths of the *shortest path between every pair of galaxies*. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.


Due to something involving gravitational effects, *only some space expands*. In fact, the result is that *any rows or columns that contain no galaxies* should all actually be twice as big.


In the above example, three columns and two rows contain no galaxies:



```
   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^

```

These rows and columns need to be *twice as big*; the result of cosmic expansion therefore looks like this:



```
....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......

```

Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:



```
....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......

```

In these 9 galaxies, there are *36 pairs*. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one `.` or `#` at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)


For example, here is one of the shortest paths between galaxies `5` and `9`:



```
....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......

```

This path has length `*9*` because it takes a minimum of *nine steps* to get from galaxy `5` to galaxy `9` (the eight locations marked `#` plus the step onto galaxy `9` itself). Here are some other example shortest path lengths:


* Between galaxy `1` and galaxy `7`: 15
* Between galaxy `3` and galaxy `6`: 17
* Between galaxy `8` and galaxy `9`: 5


In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is `*374*`.


Expand the universe, then find the length of the shortest path between every pair of galaxies. *What is the sum of these lengths?*



To begin, [get your puzzle input](11/input).


Answer:  


You can also [Shareon
 [Twitter](https://twitter.com/intent/tweet?text=%22Cosmic+Expansion%22+%2D+Day+11+%2D+Advent+of+Code+2023&url=https%3A%2F%2Fadventofcode%2Ecom%2F2023%2Fday%2F11&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void(0);)] this puzzle.





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



