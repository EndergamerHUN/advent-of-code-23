conversions: list[dict[list, int]] = []
seeds: list[int] = []

def convert(input: int) -> int:
  output = input
  for conversion in conversions:
    for key in conversion.keys():
      if output in key:
        output = conversion[key] + key.index(output)
        break
  return output


with open("day_5\\input.txt", 'r') as file:
  seeds = []
  data = list(map(int, file.readline().split(": ")[1].split()))
  for pair in list(zip(data[::2],data[1::2])):
    print(pair)
    seeds.append(range(pair[0],pair[0]+pair[1]))
  
  while True:
    line = file.readline()
    if line == '': break
    if ':' in line:
      mapping = {}
      while True:
        line = file.readline()
        if line in ['','\n']: break
        data = list(map(int, line.split()))
        mapping[range(data[1],data[1]+data[2])] = data[0]
      conversions.append(mapping)

minimum = float('inf')
for range in seeds:
  print("New range:",range)
  for seed in range:
    number = convert(seed)
    if number < minimum:
      minimum = number

print(minimum)