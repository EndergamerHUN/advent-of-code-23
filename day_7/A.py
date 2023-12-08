import functools

strengths = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
def strongerCard(a: str, b: str) -> bool:
  for i in range(5):
    ra = strengths.index(a[i])
    rb = strengths.index(b[i])
    if ra == rb: continue
    return ra > rb
  return True

@functools.total_ordering
class Hand:
  def __init__(self, hand: str):
    self.hand = hand
    count = {}
    for card in hand:
      try:
        count[card] += 1
      except KeyError:
        count[card] = 1
    count = list(count.values())
    count.sort(reverse=True)
    if count[0] > 3:
      self.rank = count[0]+1
    elif count[0] == 3:
      self.rank = 3 + (count[1] == 2)
    elif count[0] == 2:
      self.rank = 1 + (count[1] == 2)
    else:
      self.rank = 0
  
  def __str__(self) -> str:
    return self.hand

  def __eq__(self, other) -> bool:
    if isinstance(other, Hand):
      return False
    return self.hand == other.hand
  
  def __gt__(self, other) -> bool:
    if self.rank == other.rank:
      return strongerCard(self.hand, other.hand)
    return self.rank > other.rank
  

hands = []
with open("day_7\\input.txt",'r') as file:
  for line in file:
    data = line.split()
    hands.append([Hand(data[0]), int(data[1])])
hands.sort()

sum = 0
for i, hand in enumerate(hands):
  sum += (i+1)*hand[1]
print(sum)