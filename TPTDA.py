##Lo que quise hacer fue Escriba un programa que permita crear una lista de palabras 
##y que, a continuación de tres opciones:
#Cortar
#Modificar
#Mostrar
#Eliminar
#()TERMINAR

##Almaceno los valores ingresados por el usuario
lista = []
#Pido ingresar dicho valor
cadena = input("Introduce una cadena. (*para teminar):")
#Mientras no se cumpla dicha opcion el programa sigue.
while cadena != "*":
    ##Agrega una cadena al final de la lista
    lista.append(cadena)
    cadena = input("Introduce una cadena. (*para teminar):")
#Muestro al usuario un Menu una vez alla finalizada el bucle de arriba
while True:
    def menu():
        
        print("\n")
        print("1. Contar")
        print("2. Modificar")
        print("3. Eliminar")
        print("4. Mostrar")
        print("5. Salir")
    menu()
    #Pido que me diga una opcion correspondiente al menu, si la opcion que ingreso no esta
    #se le menciona que ingreso un valor incorrecto
    opcion = int(input("Dime opción:"))
    if opcion == 1:
        cadena = input("Introduce una cadena a buscar:")
        print("La cadena aparece %d veces" % lista.count(cadena))
    elif opcion == 2:
        cadena = input("Introduce una cadena a buscar:")
        cadena2 = input("Introduce una cadena a modificar:")
        indice = 0
        for elemento in lista:
            if elemento == cadena:
                lista[indice] = cadena2
            indice += 1
    elif opcion == 3:
        cadena = input("Introduce una cadena a eliminar:")
        if cadena in lista:
            while cadena in lista:
                lista.remove(cadena)
        else:
            print("No existe la cadena en la lista.")
    elif opcion == 4:
        for elemento in lista:
            print(elemento," ",end="")
    elif opcion == 5:
        print("Gracias por participar....")
        break
    else:
        print("Opción incorrecta")
