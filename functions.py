import random

string_array = ["Java", "C++", "Python"]

def add(x, y):
  return x + y

def randNum():
  return random.randint(100, 200)

def word():
  return string_array[random.randint(0, 2)]

print(add(3, 2))
print(randNum())
print(word())