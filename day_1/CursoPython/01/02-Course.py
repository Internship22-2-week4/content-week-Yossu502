# Strings 

from tkinter import N


country = 'Guatemala'
secondLetter =  country[1]
otherLetter = 'u'
print(id(secondLetter))
print(id(otherLetter))

# Operaciones con strings

platzi = 'platzi'
platzi.upper()
platzi.find('z')
platzi.startswith('pl')


# Slices 

myName = 'ferrocarril'
myName[0:3] # Desde el indice cero hasta 3
myName[::2] # De par en par
myName[3:3]
myName[:]
myName[1:-1:2]
myName[::-1]

# For Loops and while Loops

""" for i in range(10):
  print(i) """

n = 5

while n > 0:
  print(n)
  n -=1