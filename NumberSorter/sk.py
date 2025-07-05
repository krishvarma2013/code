import random
numbers = []
for i in range(100):
  numbers.append(random.randint(0,50))
print(numbers)
for i in range(len(numbers)):
  smallestIndex = i
  for j in range(i, len(numbers)):
    if numbers[smallestIndex] > numbers[j]:
      smallestIndex = j
  temp = numbers[i]
  numbers[i] = numbers[smallestIndex]
  numbers[smallestIndex] = temp

print(numbers)