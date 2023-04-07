import random

choice = random.randint(1, 3)
if choice == 1:
    rock = '''
      _______________
     /               \\
    |       ROCK     |
    \________________/
    '''
    print(rock)
if choice == 2:
    rock = '''
        /^\\
       /   \\
      /     \\
      |     |
      |     |
      |     |
      |     |
      |     |
    /  \   /  \\
   |    |  |   |
   ------  -----
    '''
    print(rock)