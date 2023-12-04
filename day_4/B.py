sum = 0
games = []
with open("day_4/input.txt",'r') as file:
  for game in file.readlines():
    data = game.split(': ')[1].split(" | ")
    matches = 0
    winning = data[0].split()
    numbers = data[1].split()
    for number in numbers:
      if number in winning:
        matches += 1
    games.append(matches)

copies = [1 for i in range(len(games))]
print(copies)

def scratch(i:int):
  if i > len(games): return
  copy = copies[i]
  global sum
  sum += copy
  for j in range(i+1, i+games[i]+1):
    copies[j] += copy

for i in range(len(games)):
  scratch(i)

print(sum)

