
sum = 0
maximum = {
  "red": 12,
  "green": 13,
  "blue": 14
}
with open("day_2/input.txt",'r') as file:
  for i, line in enumerate(map(str.rstrip, file)):
    data = line.split(": ")[1]
    possible = True
    for cubes in data.split("; "):
      for cube in cubes.split(", "):
        (amount, color) = cube.split(" ")
        if int(amount) > maximum[color]:
          possible = False
          break
      if not possible: break
    if possible:
      sum += i+1
print(sum)