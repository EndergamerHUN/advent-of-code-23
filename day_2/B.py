sum = 0
with open("day_2/input.txt",'r') as file:
  for i, line in enumerate(map(str.rstrip, file)):
    maxi = {
      "red": 0,
      "green": 0,
      "blue": 0
    }
    data = line.split(": ")[1]
    possible = True
    for cubes in data.split("; "):
      for cube in cubes.split(", "):
        (amount, color) = cube.split(" ")
        maxi[color] = max(maxi[color], int(amount))
    sum += maxi["red"] * maxi["green"] * maxi["blue"]
print(sum)