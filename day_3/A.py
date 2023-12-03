def clamp(minimum: int, num: int, maximum: int) -> int:
  return max(minimum, min(num, maximum))

def near_special(lines, i: int, j: int, length: int) -> bool:
  for y in range(i-1, i+2):
    for x in range(j-length-1, j+1):
      xId = clamp(0, x, len(lines[i])-1)
      yId = clamp(0, y, len(lines)-1)
      char = lines[yId][xId]
      if char != '.' and char != '\n' and not char.isalnum():
        print(lines[yId][xId], "not alnum")
        return True
  return False

sum = 0
with open("day_3/input.txt",'r') as file:
  lines = file.readlines()
  for i, line in enumerate(lines):
    j = 0
    while j < len(line):
      number = ""
      while line[j].isdigit():
        number += line[j]
        j += 1
      if number != "":
        if near_special(lines, i, j, len(number)):
          sum += int(number)
      j += 1

print(sum)