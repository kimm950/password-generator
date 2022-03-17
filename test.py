#! /usr/bin/python
import random

print('welcome')

chars = '34512351345tbejkglbndfhjgbvsdfjhbvuisbglvsj'
chars

print(chars)


number = input('Amount of passwords to generate: ')
print(type(number))
number = int(number)

length = input('Input your passcode: ')
length = int(length)

print('sup \n\n\n\n\n\n\n\n\nhere are your passcode: ')

for pscode in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)

