#son similares a los objetos en Java , se definen con {}

persona = {'name': 'Gabriel', 'last_name': 'Roman', 'age': 32}

print(persona,'\n')
print(persona['name'],'\n')

#si se empieza con " dentro usar '
print(f"Hola mi nombre es {persona['name']} y tengo {persona['age']} años",'\n')
#si se empieza con ' dentro usar "
print(f'Hola mi nombre es {persona["name"]} y tengo {persona["age"]} años','\n')

persona['city'] = "Caseros"
print(persona,'\n')

#para borrar usar la plabra reservada del - ejemplo: del persona['age']

print(len(persona))

#con la palabra reservada len , nos dira la cantidad de claves que tenemos