
def calcularImpuestos(age, incomes):
  if (age >= 18) and (incomes >= 1000):
    return incomes * 0.40
  else:
    return 0


if __name__ == '__main__':
  print(calcularImpuestos(18, 1000)) # 400
  print(calcularImpuestos(40, 10000)) # 4000
  print(calcularImpuestos(17, 5000)) # 0
  print(calcularImpuestos(30, 500)) # 0