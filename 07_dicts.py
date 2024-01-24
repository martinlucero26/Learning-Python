### Dictionaries ###

#Hay una relación clave-valor --> Nombre:Martin

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Martin", "Apellido":"Lucero", "Edad":20, 1:"Cruzzi"}
print(my_other_dict)

my_dict = {"Nombre":"Martin",
           "Apellido":"Lucero",
           "Edad":20,
           "Singers":{"Cruzzi", "Badbo", "Felcho"},
           1:1.78}

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Singers"])

my_dict["Nombre"] = "Carlos" #Cambia el valor de la clave
print(my_dict)

my_dict["Singers"].add("Jesse")
print(my_dict)