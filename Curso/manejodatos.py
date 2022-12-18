name = input("Ingrese Nombre: ")
print(f"Hola {name} como estas?",'\n')

num1 = input("Ingrese un valor: ")
num2 = input("Ingrese otro valor: ")

#al ingresar valores , se toman como strings y deben convertirse , pueden convertirse en el mismo input si se encierra ej: int(input("Ingrese un valor: "))
"""
float() para convertir en decimales
int() para convertir a enteros
str() para convertir a texto
bool() para convertir en booleano (true o false)
"""
resultado = int(num1) + int(num2)
print(f"La suma de los valores ingresados es: {resultado}",'\n')