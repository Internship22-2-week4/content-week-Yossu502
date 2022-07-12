def contrasenaValida(password):
  if (password == '2Fj(jjbFsuj') or (password == 'eoZiugBf&g9'):
    return True
  else:
    return False



if __name__ == '__main__':
  password = input('Introduzca su contraseña por favor: ')
  print(contrasenaValida(password))
