#Juego del ahorcado
#
dificultad = input("¿Qué dificultad quiere para el juego? baja/media/alta: ")
if dificultad == 'baja':
    lista = ['listi']
    cadena = "-" * len(lista)
    intentos = 0
    while True:
        def busqueda_lineal (lista, letra):
            for i in range (len(lista)):
                if lista [i] == letra:
                    cadena = cadena [i] + letra + cadena [i + 1]
                else:
                    if intentos == 1:
                        print(" O")
                    elif intentos == 2:
                        print(" O")
                        print("/")
                    elif intentos == 3:
                        print(" O")
                        print("/ |")
                    elif intentos == 4:
                        print(" O")
                        print("/ | \\ ")
                    elif intentos == 5:
                        print(" O")
                        print("/ | \\ ")
                        print("/ ")
                    elif intentos == 6:
                        print(" O")
                        print("/ | \\ ")
                        print("/ \\")
                        print(f"Perdiste el juego, la palabra era, {lista}")

                if cadena == lista:
                    print(f"¡Felicidades, ganaste el juego! la palabra es, {lista}")
                    break

letra = input("Ingresa una letra ")
