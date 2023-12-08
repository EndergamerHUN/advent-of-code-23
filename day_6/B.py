import math

with open("day_6\\input.txt",'r') as file:
  time = int(file.readline().split(":")[1].replace(" ", ""))
  dist = int(file.readline().split(":")[1].replace(" ", ""))
  for i in range(1,math.floor(time/2)):
    if i*(time-i) > dist:
      sum = time-2*i+1
      break
  print(sum)