import functools

ranking = [
  [5],
  [4],
  [3, 2],
  [3],
  [2, 2],
  [2],
]
strengths = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
def strongerCard(a: str, b: str) -> bool:
  for i in range(5):
    ia = strengths.index(a[i])
    ib = strengths.index(b[i])
    if ia == ib: continue
    return ia > ib
  return True

def can_make(attempt: list[int], count: list[int], joker: int) -> bool:
  count = count.copy()
  for num in attempt:
    try:
      if (count[0] + joker) < num:
        return False
      count.pop(0)
      joker -= max(0, num-count[0])
    except IndexError:
      return False
  return True

@functools.total_ordering
class Hand:
  def __init__(self, hand: str):
    self.hand = hand
    count = {}
    joker = 0
    for card in hand:
      if card == 'J':
        joker += 1
      else:
        try:
          count[card] += 1
        except KeyError:
          count[card] = 1
    count = list(count.values())
    count.append(0)
    count.sort(reverse=True)
    for i, attempt in enumerate(ranking):
      if can_make(attempt, count, joker):
        break
    self.rank = 6-i

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