PASSWORD = '12345'


def passwordRequired(func):
  def wrapper():
    password = input('Cual es tu contraseña? ')
    if password == PASSWORD:
      return func()
    else:
      print('La contraseña no es correcta')
  return wrapper

@passwordRequired
def need_password():
  print('La contraseña es correcta')

if __name__ == '__main__':
  need_password()