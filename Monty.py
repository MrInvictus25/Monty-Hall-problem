import itertools
import random
def WithoutChange(three_doors):
  choice = random.choice(range(len(three_doors)))
  return three_doors[choice]
# result = WithoutChange(three_doors)
# print(result)

def WithChange(three_doors):
  the_first_choice = random.choice(range(len(three_doors)))
  for i in range(len(three_doors)):
    if i != the_first_choice and three_doors[i] != 'Car':
      opened_door = i
      #print(i)
      break
  #print(opened_door)
  for item in range(len(three_doors)):
    if item != the_first_choice and item != opened_door:
      the_second_choice = item    
      return three_doors[the_second_choice]

Attempt = 10000
three_doors = ['Car', 'Goat', 'Goat']

CountWin_WithoutChange = 0
CountWin_WithChange = 0
for num in range(Attempt):
  random.shuffle(three_doors)
  
  if WithoutChange(three_doors) == 'Car':
    CountWin_WithoutChange += 1

for num in range(Attempt):
  random.shuffle(three_doors)

  if WithChange(three_doors) == 'Car':
    CountWin_WithChange += 1
print(CountWin_WithoutChange/Attempt)
print(CountWin_WithChange/Attempt)