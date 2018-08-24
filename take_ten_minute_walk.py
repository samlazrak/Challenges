import random

def isValidWalk(walk):
  if len(walk) > 10 or len(walk) < 10:
    return False
  elif len(walk) == 10:
    map = [['.' for x in range(10)] for x in range(10)]
    position = [4, 4]
    map[position[0]][position[1]] = 'b'
    iter = 0
    for i in walk:
      iter = iter+1
      if i == 'n':
        if position[0] != 0 and position[0] != 9:
          position[0] = position[0]-1
        map[position[0]][position[1]] = 'n'
        if iter == 10 and position == [4, 4]:
          print('Valid walk: '+walk)
          return True
      elif i == 'e':
        if position[1] != 0 and position[1] != 9:
          position[1] = position[1]-1
        map[position[0]][position[1]] = 'e'
        if iter == 10 and position == [4, 4]:
          print('Valid walk: '+walk)
          return True
      elif i == 's':
        if position[0] != 0 and position[0] != 9:
          position[0] = position[0]+1
        map[position[0]][position[1]] = 's'
        if iter == 10 and position == [4, 4]:
          print('Valid walk: '+walk)
          return True
      elif i == 'w':
        if position[1] != 0 and position[1] != 9:
          position[1] = position[1]+1
        map[position[0]][position[1]] = 'w'
        if iter == 10 and position == [4, 4]:
          print('Valid walk: '+walk)
          return True

def create_tests(count):
  letters = ['n', 's', 'e', 'w']
  walk = ''.join(random.choice(letters) for i in range(count))
  return walk

def test():
  for i in range(999):
    validWalk = isValidWalk(create_tests(random.randint(0,20)))

test()