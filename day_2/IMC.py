def bmi(peso, altura):
  imc = peso / (altura**2)
  if imc < 18.5:
    return 'Bajo de peso'
  
  elif 18.5 <= imc < 24.9:
    return 'Normal'

  elif 25 <= imc < 29.9:
    return 'Sobrepeso'
  
  elif imc >= 30:
    return 'Obeso'
    
  else:
    return 'Datos no correctos'

if __name__ == '__main__':
    print(bmi(65, 1.8)) # "Normal"
    print(bmi(72, 1.6)) # "Sobrepeso"
    print(bmi(52, 1.75)) #  "Bajo de peso"
    print(bmi(135, 1.7)) # "Obeso"