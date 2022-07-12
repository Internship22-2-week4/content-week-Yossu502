def contrasenaValida(password):
  if (password == '2Fj(jjbFsuj') or (password == 'eoZiugBf&g9'):
    return True
  else:
    return False



if __name__ == '__main__':
  print(contrasenaValida("2Fj(jjbFsuj")) # true
  print(contrasenaValida("eoZiugBf&g9")) # true
  print(contrasenaValida("hola")) # false
  print(contrasenaValida(""))
