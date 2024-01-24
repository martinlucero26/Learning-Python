### Strings ###
""""
my_string = "Mi String"
my_other_string = 'Mi string'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_escape_string = "\t Este es un string \n escapado"
print(my_escape_string)

# Formateo

name, surname, age = "Martin", "Lucero", 20

print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")
"""

# Desempaquetado de caracteres
language = "Python"
a,b, c, d, e, f = language

print(a)
print(e)


# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

# Reverse

reverse_language = language[::-1]
print(reverse_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.upper().isupper())
print(language.lower())
print(language.count("y"))
print(language.isnumeric())
print("1".isnumeric())
print(language.startswith("Py"))


