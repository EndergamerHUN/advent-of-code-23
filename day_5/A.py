conversions: list[dict[list, int]] = []
seeds: list[int] = []

def convert(input: int) -> int:
  output = input
  for i, conversion in enumerate(conversions):
    for key in conversion.keys():
      if output in key:
        output = conversion[key] + key.index(output)
        break
  return output


with open("day_5\\input.txt", 'r') as file:
  seeds = list(map(int, file.readline().split(": ")[1].split()))
  
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
for seed in seeds:
  minimum = min(convert(seed), minimum)

print(minimum)