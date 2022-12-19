# pass se utiliza si la clase esta vacia

class Coche: #objeto
  marca = ""
  color = "Blanco"
  __encendido = False #con los dos guiones bajos, encapsulamos
  __apagado = True
  velocidad = 0
  
  def __init__(self, marca, color): #metodos
    self.marca = marca
    self.color = color
    
  def encender(self):
    self.__encendido = True
    self.__apagado = False
    
  def set_velocidad(self, V):
    self.velocidad = V
    
  def get_encendido(self):
    return self.__encendido

  def get_apagado(self):
    return self.__apagado

class Coche4x4: 
  PRuedas = 19

class CocheDeportivo(Coche, Coche4x4): #Herencia  #Herencia-multiple
  cv = 60

  def __init__(self, marca, color, cv, PRuedas):
    self.marca = marca
    self.color = color
    self. cv = cv
    self.PRuedas = PRuedas
