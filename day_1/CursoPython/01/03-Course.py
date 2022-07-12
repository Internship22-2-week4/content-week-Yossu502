from asyncore import read
import copy
import random
# Listas 

countries = ['Mexico', 'Venezuela', 'Colombia', 'Argentina']
ages = [12, 18, 24, 42, 50]
weights = [24, 18, 50, 35, 4 ,8]

global_country = countries
countries[0] = 'Guatemala'
global_country =  copy.copy(countries)
countries[1] = 'EE.UU.'
""" print(global_country)
print(countries)
 """
# Operaciones con listas

a = [1, 2]
b = [2, 3]
c = a + b
d = a * 3
""" print(d) """

# append agrega elemntos al final de la lista
countries.append('Alemania')
""" print(countries) """

# pop elimina el ultimo elemnto de la lista, ademas que lo regresa

country_out =  countries.pop()
""" print(country_out) """

# Sort, ordena una nueva lista con una nueva instancia

weights.sort()
""" print(weights)
print(len(countries)) """

# del 

del countries[2]
# print(countries)

# Diccionarios

rae = {}
rae['Pizza'] = 'La comida mas deliciosa del mundo'

rae['Pasta'] = 'Comida italiana de distintas formas de hacerla'
print(rae)

print(rae.get('helado', None))

# print(rae.keys())
# print(rae.values())
# print(rae.items())

for key in rae.keys():
  print(key)

for value in rae.values():
  print(value)

for key, value in rae.items():
  print(key, value)


# Tuplas

a = (1, 2, 3, 4, 5, 6, 7, 3, 3, 3, 2, 89, 2, 1, 98)
print(a.count(2)) # Cuenta cuantos valores esta adentro de ese tuple
print(a.index(89))


# Sets

conjuntoA = set([1, 2, 3])
conjuntoB = set([3, 4, 5])
conjuntoA.add(20)
# print(conjuntoA)
# print(conjuntoA.intersection(conjuntoB))
# print(conjuntoA.union(conjuntoB))
# print(conjuntoB.difference(conjuntoA))
conjuntoA.remove(20)
# print(conjuntoA)

# Comprehensions 

lista = list(range(100))
pares = [numero for numero in lista if numero % 2 == 0]
print(pares)

studen_uid = [1, 2, 3]
students = ['Juan', 'Jose', 'Larsen']
studentsWithUid = {uid: student for uid, student in zip(studen_uid, students)}
print(studentsWithUid)

randomNumber = []
for i in range(10):
  randomNumber.append(random.randint(1,3))

nonRepeated = {number for number in randomNumber}
print(nonRepeated)

# Busqueda Binaria 
