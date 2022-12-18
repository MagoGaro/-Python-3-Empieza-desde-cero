numeros = [1, 55, 88, 43, 4, 7, 9, 22, 0]

array20items = range(0,20)

for num in numeros:
  print(num, end=" ") #con el end, podemos imprimir uno al lado del otro
print('\n')
for num in array20items:
  print(num, end=" ")
print('\n')
print('A continuacion le pediremos unos datos para confeccionar una tabla de multiplicar','\n')

tabla = int(input('Ingrese el valor de su tabla: '))
print('\n')
nums = range(1,11)
print('=== Tabla hecha con For ===')
for num in nums:
  print(f'{tabla} x {num} = {tabla*num}')

#################### while ################
print('\n','\n')
print('=== Tabla hecha con While ===')
x = 1
while x <= 10:
  print(f'{tabla} x {x} = {tabla*x}')
  x+=1 #nunca olvidarse del acumulador ! no funciona el ++ como en otros lenguajes