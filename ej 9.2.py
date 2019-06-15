#inventado
telefono = input("introduce tu numero de telefono: ")
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for numero in numeros: 
    veces = 0
    for n in telefono:
        if n == numero:
            veces += 1
    print("el numero de telefono contiene el numero " + str(numero) + " " + str(veces) + " veces")
