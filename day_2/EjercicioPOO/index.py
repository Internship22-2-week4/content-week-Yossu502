from ObraDeArte import ObraDeArte

class Portafolio:
  
  def __init__(self, name) :
    self.nombrePortafolio = name
    self.obrasArte= []
    self.expoArt = None

  
  def registrarObra(self, obra):
    obraNew = ObraDeArte(obra)
    self.obrasArte.append(obraNew)

  
  def registrarNuevaExposicion(self, expo):
    self.expoArt = Exposicion(expo)
    for obra in self.obrasArte:
      self.expoArt.addArtworks(obra)

 
  def mostrarExpo(self):
    print(self.expoArt)


  def mostrarObras(self):
    for obra in self.obrasArte:
      print(obra)

  def getName(self):
    return f'{self.nombrePortafolio}'



class Exposicion():
  def __init__(self, expo):
    self.name = expo['nombre']
    self.date = expo['fecha']
    self.place = expo['lugar']
    self.description = expo['descripcion']
    self.artworks = []

  def addArtworks(self, obra):
    self.artworks.append(obra)


  def __str__(self) -> str:
    return f'{self.name}, {self.date}, {self.place}, {self.description}, {self.artworks}'



obraDeArte = {
  'name': 'MonaLisa',
  'type': 'Pintura',
  'authors': ['Salvador Dali', 'Pablo Picasso', 'Vicente'],
  'date': '17/05/1785',
  'price': '5890',
  'photos': ['www.google/mona.com', 'www.yotube/mona.com']
}

obraDeArte2 = {
  'name': 'El grito',
  'type': 'Escultura',
  'authors': ['Miguel Angel'],
  'date': '25/12/1895',
  'price': '6500',
  'photos': ['www.google/grito.com', 'www.yotube/grito.com']
}

obraDeArte3 = {
  'name': 'Roma',
  'type': 'Video',
  'authors': ['Salvador Dali', 'Pablo Picasso', 'Vicente'],
  'date': '2/05/1775',
  'price': '10500',
  'photos': ['www.google/mRomaona.com', 'www.yotube/Roma-png.com']
}

exposicion = {
  'nombre': 'Exposicion Nuevas Artes',
  'fecha': '02/10/2022',
  'lugar': 'Huehuetenango, Guatemala',
  'descripcion': 'Exposicion para dar a conocer los nuevos talentos.'
}

Portafolio1 = Portafolio('Portafolio Pinturas')
Portafolio1.registrarObra(obraDeArte)
Portafolio1.registrarObra(obraDeArte2)
Portafolio1.registrarObra(obraDeArte3)
Portafolio1.registrarNuevaExposicion(exposicion)
print(f'Obras de Arte del portafolio: {Portafolio1.getName()}')
print('*' * 175)
Portafolio1.mostrarObras()
print('*' * 175)
Portafolio1.mostrarExpo()