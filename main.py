# Abdullah Alshawa
import random

print('Welcome')
# 0 is rock, 1 is paper, and 2 is scissors
r = random.randint(0, 2)
prmpt = input('Rock, paper, or scissors?')
if prmpt == 'Rock' and r == 0:
    print('You choose Rock')
    print('Computer choose Rock')
    print('Draw')
    exit()
if prmpt == 'Rock' and r == 1:
    print('You choose Rock')
    print('Computer choose paper')
    print('Lost')
    exit()
if prmpt == 'Rock' and r == 2:
    print('You choose Rock')
    print('Computer choose scissors')
    print('Won')
    exit()

if prmpt == 'Paper' and r == 0:
    print('You choose Paper')
    print('Computer choose Rock')
    print('Won')
    exit()
if prmpt == 'Paper' and r == 1:
    print('You choose Paper')
    print('Computer choose paper')
    print('Draw')
    exit()
if prmpt == 'Paper' and r == 2:
    print('You choose Paper')
    print('Computer choose scissors')
    print('Lost')
    exit()

if prmpt == 'Scissors' and r == 0:
    print('You choose Scissors')
    print('Computer choose Rock')
    print('Lost')
    exit()
if prmpt == 'Scissors' and r == 1:
    print('You choose Scissors')
    print('Computer choose paper')
    print('Won')
    exit()
if prmpt == 'Scissors' and r == 2:
    print('You choose Scissors')
    print('Computer choose scissors')
    print('Draw')
    exit()

print('Goodbye')
