#!/usr/bin/env python
# coding: utf-8

# In[18]:

#Dice Game
import random
n= int(input('Enter number of dice: '))
def rolldice(n):
    dice=[]
    for i in range(n):
        dice.append(random.randint(1,6))
    total=0
    for num in dice:
        total=total+num
    return total,dice
mytotal,myroling=rolldice(n)
print('Your roll:',myroling,'=',mytotal)
computertotal,computer_roll=rolldice(n)
print('computers roll:',computer_roll,'=',computertotal)
if (computertotal>mytotal):
    print('You lost! Computer Won!')
elif (computertotal<mytotal):
    print('YOU WON!!')
elif (computertotal==mytotal):
    print('It Was a Tie.')

