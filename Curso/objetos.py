#import coche #importamos el archivo completo

from coche import Coche, CocheDeportivo #solo importamos la clase

# una de las formas de utilziarlo es poner el archivo.elobjeto ejemplo coche.Coche

coche1 = Coche("Fiat", "Gris")
coche2 = Coche("Renault", "Azul")
coche1.encender()
coche1.set_velocidad(60)

coche3 = CocheDeportivo("Chevrolet", "Rojo", 461, 20)

if coche1.get_encendido() and not coche1.get_apagado():
  print(f'El {coche1.marca} esta encendido y va a {coche1.velocidad} Km/h \n')
else:
  print(f'El {coche1.marca} esta apagado \n')



print(f'El {coche1.marca} es de color {coche1.color} \n')
print(f'El {coche2.marca} es de color {coche2.color} \n')
print(f'El {coche3.marca} es de color {coche2.color} , tiene {coche3.cv} CV y unas ruedas de {coche3.PRuedas} "\n')


