# se definen con []
list = ["Python","Django","React","Java","C","C++","C#"]
print(list,'\n')
print(list[3],'\n')
print(list[-1],'\n') #al usar el menos(-) empezara desde la derecha hacia la izquierda

list[1] = "Node.js" # reemplaza en el indice indicado

print(list,'\n')

list.append("Sql") # añade al final de la lista
print(list[-1],'\n')
print(list,'\n')

list.insert(1, "Django") # añade en el indice indicado
print(list,'\n')