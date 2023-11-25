import calc
print("Bienvenido, puede elegir entre las siguientes opciones")
while True:
    print('''
Presione 1 para introducir una valoracion
Presione 2 para comprobar el registro de valoraciones hasta la fecha
Presione 3 para salir del programa''') 
    num = input() 
    if num.isdecimal():
        num=int(num)
        if num==1:
            calc.save()
        elif num==2:
            calc.show()
        elif num==3:
            print("TERMINACION")
            break 
        else: 
            print("Por favor, introduzca del 1 a 3")
    else: 
        print("Por favor, introduzca del 1 a 3")

print("Gracias por utilizar mi programa")
