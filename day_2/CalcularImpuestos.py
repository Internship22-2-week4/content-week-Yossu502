
def calcularImpuestos(age, incomes):
  if (age >= 18) and (incomes >= 1000):
    return incomes * 0.40
  else:
    return 0


if __name__ == '__main__':
  age = int(input('Introduzca su edad por favor: '))
  incomes = int(input('Introduzca sus ingresos por favor: '))
  taxes = calcularImpuestos(age, incomes)
  print(taxes)