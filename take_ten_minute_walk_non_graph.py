import random

def isValidWalk(walk):
  position = [0, 0]
  iter = 0
  for i in walk:
    iter = iter+1
    if i == 'n':
      position[1] = position[1]+1
      if iter == 10:
        if position == [0, 0]:
          print('Valid walk')
    if i == 's':
      position[1] = position[1]-1
      if iter == 10:
        if position == [0, 0]:
          print('Valid walk')
    if i == 'e':
      position[0] = position[0]+1
      if iter == 10:
        if position == [0, 0]:
          print('Valid walk')
    if i == 'w':
      position[0] = position[0]-1
      if iter == 10:
        if position == [0, 0]:
          print('Valid walk')
  print(position)

def create_tests(count):
  letters = ['n', 's', 'e', 'w']
  walk = ''.join(random.choice(letters) for i in range(count))
  return walk

def test():
  for i in range(999):
    isValidWalk(create_tests(10))

test()