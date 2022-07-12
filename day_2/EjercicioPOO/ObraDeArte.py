class ObraDeArte:
  def __init__(self, diccionarioObra):
    self.nombre = diccionarioObra['name']
    self.tipo = diccionarioObra['type']
    self.autores = diccionarioObra['authors']
    self.fecha = diccionarioObra['date']
    self.valor = diccionarioObra['price']
    self.fotoVideo = diccionarioObra['photos']
  
  def __str__(self) -> str:
    return f'Nombre: {self.nombre}\n Tipo de arte: {self.tipo}\n Autores: {self.autores}\n Fecha publicacion:{self.fecha}\n  Precio: {self.valor}\n Fotos o videos:{self.fotoVideo}'