### Tuples ###

my_tuple = tuple() #Formas de declarar una tupla
my_other_tuple = () #Formas de declarar una tupla

my_tuple = (20, 1.78, "Martín", "Lucero") #Asignar valores a una tupla
 
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count(20)) #Mientras que el len cuenta la cantidad de elementos que hay en esa tupla, el count cuenta la cantidad de veces que aparece un elemento en la tupla
print(my_tuple.index("Lucero")) #El 'Index' me va a retornar el índice del elemento que yo le indique


#my_tuple[1] = 1.80 Esto da un error porque una tupla es inmutable
#print(my_tuple) TypeError: 'tuple' object does not support item assignment

my_other_tuple = (20, 56, 31)
print(my_other_tuple)

print(my_tuple + my_other_tuple)

my_new_tuple = my_tuple + my_other_tuple
print(my_new_tuple)

del my_new_tuple[2] #TypeError: 'tuple' object doesn't support item deletion

del my_new_tuple #Eliminar una tupla
#print(my_new_tuple) NameError: name 'my_new_tuple' is not defined
