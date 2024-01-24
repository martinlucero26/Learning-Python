### Variables ###

my_string_variable = "My String Variable"
#print(my_string_variable)

my_int_variable = 5
#print(my_int_variable)

my_bool_variable = False
#print(my_bool_variable)

#print(my_string_variable, my_int_variable, my_bool_variable)

# Pasando una variable entera a str con la función str:
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

# Type de un Print: Tipo 'NoneType'. Print es una función del sistema, no tiene ningún tipo de dato
print(type(print("Mi cadena de texto")))

# Algunas funciones del Sistema:
print(len(my_int_to_str_variable)) #Cuantos caracteres tiene(longitud de la variable)

# Variables en una sola línea - ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age= "Martín", "Lucero Altamirano", 'Tincho', 20
print("Me llamo", name, surname,", tengo", age,"años",", y me dicen", alias)

# Inputs - Nos pide datos por teclado
"""
first_name = input('¿Cuál es tu nombre?: ')
age = input('¿Cuál es tu edad?: ')

print(first_name)
print(age)
"""

# Cambiamos su tipo - Podemos modificar una variable
name = 20
age = "Martín"
print(name)
print(age)

# ¿Forzamos el tipo? Python tiene un tipado dinámico

address: str = "Mi dirección"
address = 32
print(address)