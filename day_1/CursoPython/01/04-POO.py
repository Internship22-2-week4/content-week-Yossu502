class Persona:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age
  
  def sayHello(self):
    print(f'Hello, my name is {self.name} and my age is: {self.age}')



if __name__ == '__main__':
  person = Persona('Josue', 23)
  print(person.sayHello())