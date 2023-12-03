def clamp(minimum: int, num: int, maximum: int) -> int:
  return max(minimum, min(num, maximum))

def get_ratio(lines: list[str], i: int, j: int) -> list[tuple[int]]:
  locs = []
  for y in range(i-1,i+2):
    x = j-1
    while x < j+2:
      if lines[y][x].isdigit():
        locs.append((x, y))
        while x != len(lines[y]) and lines[y][x+1].isdigit():
          x += 1
      x += 1
  return locs

def count_ratio(lines: list[str], locs: list[tuple[int]]) -> int:
  mult = 1
  for x, y in locs:
    while lines[y][x-1].isdigit():
      x -= 1
    number = ""
    while lines[y][x].isdigit():
      number += lines[y][x]
      x += 1
    mult *= int(number)
  return mult    


sum = 0
with open("day_3/input.txt",'r') as file:
  lines = file.readlines()
  for i, line in enumerate(lines):
    for j, char in enumerate(line):
      if char == '*':
        locs = get_ratio(lines, i, j)
        if len(locs) == 2:
          sum += count_ratio(lines, locs)
print(sum)