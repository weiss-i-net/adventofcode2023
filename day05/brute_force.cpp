#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdint>
#include <ranges>

uint64_t map_function(const auto &m, uint64_t v) {
  for (auto& line : m) {
    uint64_t dst_start = line[0];
    uint64_t src_start = line[1];
    uint64_t length = line[2];
    if (src_start <= v && v < src_start + length) {
      return dst_start + v - src_start;
    }
  }
  return v;
}

int main() {
  std::ifstream file("input");
  std::string line;
  std::vector<uint64_t> seeds;
  std::vector<std::vector<std::vector<uint64_t>>> maps;
  if (std::getline(file, line)) {
    std::istringstream iss(line.substr(line.find(':') + 1)); // Skip "seeds:" and read the rest
    uint64_t seed;
    while (iss >> seed) {
      seeds.push_back(seed);
    }
  }
  while (std::getline(file, line)) {
    if (line.find("map:") != std::string::npos) { // Map section header
      std::vector<std::vector<uint64_t>> map;
      while (std::getline(file, line) && !line.empty()) {
        std::istringstream line_stream(line);
        std::vector<uint64_t> row;
        uint64_t num;
        while (line_stream >> num) {
          row.push_back(num);
        }
        if (!row.empty()) {
          map.push_back(row);
        }
      }
      if (!map.empty()) {
        maps.push_back(map);
      }
    }
  }

  uint64_t min_value = UINT64_MAX;
  #pragma omp parallel for
  for (int i = 0; i < seeds.size(); i += 2) {
    auto a = seeds[i];
    auto b = seeds[i] + seeds[i+1];
    #pragma omp critical
    std::cout << "Range: [" << a << ", " << b << ")\n";
    uint64_t range_min_value = UINT64_MAX;
    for (auto v_start = a; v_start < b; v_start++) {
      auto v = v_start;
      for (auto& m : maps) {
        v = map_function(m, v);
      }
      if (v < range_min_value) range_min_value = v;
    }
    #pragma omp critical
    min_value = std::min(min_value, range_min_value);

  }
  std::cout << "Part 2: " << min_value << std::endl;

  return 0;
}

