### SETS ###

#Es una colección desordenada y sin duplicados de elementos. Los elementos dentro de un set no tienen un orden específico y no se pueden acceder mediante índices.

"""
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

# Unión
union = conjunto1 | conjunto2

# Intersección
interseccion = conjunto1 & conjunto2

# Diferencia
diferencia = conjunto1 - conjunto2

print(union)
print(interseccion)
print(diferencia)
"""

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Martin", "Lucero", 20}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Orange")
print(my_other_set) #Un set no es una estructura ordenada, por lo tanto tampoco podremos acceder a un elemento ya que no tenemos un orden

my_other_set.add("Orange")
print(my_other_set) #Un set no admite elementos repetidos

print("Lucero" in my_other_set)
print("Lucerio" in my_other_set) #Verificar existencia de un elemento

my_other_set.remove("Martin") #Eliminar datos
print(my_other_set)

my_other_set.clear() #Vacia los elementos del set pero el set sigue creado
print(my_other_set)
print(len(my_other_set))

del my_other_set #Borrar un objeto por completo
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Tincho", "Altamirano", 21}
my_list = list(my_set)
print(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Cruzzi", "Badbo", "Felcho"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)