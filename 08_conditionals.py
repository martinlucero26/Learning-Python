### Condicionales ###

my_conditional = False

if my_conditional: #Es lo mismo que poner if my_conditional == True, pero eso sería redundante
    print("Se ejecuta la condición del if")
    
    
my_conditional = 5 * 5

if my_conditional > 10 and my_conditional < 20:
    print("Es mayor que 10 y menor que 20")
elif my_conditional == 25:
    print("Es igual que 25")
else:
    print("Es menor que 10 o mayor que 20 o es distinto que 25")

print("La ejecución continúa")
    
