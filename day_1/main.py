sum = 0
strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("day_1/input.txt", 'r') as file:
  lines = file.read().splitlines()
  for line in lines:
    first = True
    last = 0
    for i in range(len(line)):
      char = line[i]
      if char.isdigit():
        last = int(char)
        if first:
          first = False
          sum += 10*int(char)
      else:
        for j, string in enumerate(strings):
          if line[i:i+len(string)] == string:
            last = j+1
            if first:
              first = False
              sum += 10*(j+1)
    sum += last
print(sum)