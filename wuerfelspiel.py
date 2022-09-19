import random

numWuerfel = 6
sumPlayer = 0

for i in range(1, numWuerfel+1):
  num = random.randint(1, 6)
  print(f"Der {i}.Wuerfel hat die Augenzahl: {num}")
  sumPlayer += num