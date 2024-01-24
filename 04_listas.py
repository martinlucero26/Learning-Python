### Lists ### Es un conjunto de datos; sirve para añadir elementos, cada uno en una posición


"""
my_list = list() #Una forma de hacer listas
my_other_list = [] #Otra forma de hacer listas

print(len(my_list)) #La longitud es 0 porque no tiene ningún elemento

my_list = [20, 18, 20, 22, 50, 31, 56, 19] # Por lo tanto, una lista es una forma de agrupar datos
print(my_list)
print(len(my_list))

my_other_list = [20, 1.78, "Martin", "Lucero"]
print(my_other_list)
print(len(my_other_list)) # La longitud es 3 porque tiene 3 elementos
print(type(my_other_list))

# Si tenemos una lista, podemos acceder a sus elementos de forma separada

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(20)) #Mientras que el len cuenta la cantidad de elementos que hay en esa lista, el count cuenta la cantidad de veces que aparece un elemento en la lista
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(age)
print(height)
print(name)
print(surname)

print(my_list + my_other_list)

my_list = "Hola Python" #Tipado dinámico --> le cambiamos el tipo de dato; my_list deja de ser una lista y pasa a ser un string
print(my_list)
print(type(my_list))

print(my_other_list)
my_other_list.append("Ferxxo") #El 'Append' me va a agregar un elemento al final de la lista
print(my_other_list)
my_other_list.insert(1, "Green") #El 'Insert' me va a insertar un elemento en una posición que yo le indique
print(my_other_list)
my_other_list.remove("Green") #El 'Remove' me va a eliminar un elemento de la lista
print(my_other_list)

#my_other_list.pop() #El 'Pop' me va a eliminar el ultimo elemento de la lista y me va a retornar ese elemento si imprimo ese pop. Me elimina el último elemento si yo no le especifico cuál quiero eliminar
print(my_other_list)
print(my_other_list.pop()) #Acá estoy sacando uno y al imprimirlo me dice cuál sacó, pero se hacen estas dos operaciones a la vez
my_other_list.pop(0) #Le estoy indicando el índice del elemento en particular que quiero quitar
print(my_other_list)

my_pop_element = my_other_list.pop(1) #Estoy guardando en una variable el elemento que sacó
print(my_pop_element)
"""

my_list = [1, 20, 4, 26]
print(my_list)

my_other_list = my_list

print(my_other_list)