import math

with open("day_6\\input.txt",'r') as file:
  races = list(zip(map(int,file.readline().split(": ")[1].split()),map(int,file.readline().split(": ")[1].split())))

sum = 1
for race in races:
  time = race[0]
  dist = race[1]
  for i in range(1,math.floor(time/2)):
    if i*(time-i) > dist:
      sum *= time-2*i+1
      break
print(sum)