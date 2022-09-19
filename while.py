import random

sum = 0
num = 0
while True:
  num = random.randint(10, 30)
  if num == 15 or num == 25:
    break
  sum += num

print(f"Zahl ist {num}")
print(f"Summe: {sum}")