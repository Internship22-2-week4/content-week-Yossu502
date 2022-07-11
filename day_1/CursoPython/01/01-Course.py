from ast import If


a = 85
a +=1

# Variables y Expresiones

message = 'How are you' # Asignacion
_age = 20 # Que es privada
PI = 3.14159 # Es una asginfacion constante
__do_not_touche = 'Something importante' # No tocar es privada y su valor puede modificar todo el programa

# Funciones

# Build Functions

toInteger = int('98')
print(toInteger)

def sumaDosNumeros(x, y):
  return x + y


# Operadores logicos
x = 2
y = 3


print (x == y)
print (x != y)
print (x >= y)
print (x <= y)

if (x < y):
  print('x es menor que y')
else:
  print('x no es menor que y')