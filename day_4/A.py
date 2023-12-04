sum = 0
with open("day_4/input.txt",'r') as file:
  for game in file.readlines():
    data = game.split(': ')[1].split(" | ")
    matches = 0
    winning = data[0].split()
    numbers = data[1].split()
    for number in numbers:
      if number in winning:
        matches += 1
    if matches != 0:
      sum += 2**(matches-1)
print(sum)
      
