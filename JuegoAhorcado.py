import random

def busqueda_lineal(lista, letra):
    for i in range(len(lista)):
        if lista[i] == letra:
            return i
    return -1

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ahorcado(intentos_usados, max_intentos):
    etapas = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    
    etapa_actual = min(len(etapas)-1, intentos_usados)
    print(etapas[etapa_actual])


palabras_por_dificultad = {
    "baja": ["listi", "gato", "casa", "perro"],
    "media": ["introduccion", "programacion", "computadora"],
    "alta": ["al pensamiento computacional", "desarrollo", "arquitectura"]
}


print("Elige la dificultad: baja / media / alta")
dificultad = input("Dificultad: ").lower()


palabra = random.choice(palabras_por_dificultad[dificultad]).lower()
letras_palabra = list(palabra)
letras_adivinadas = ['_' if letra != ' ' else ' ' for letra in letras_palabra]

max_intentos = 7
intentos_restantes = max_intentos
intentos_usados = 0  
letras_usadas = []

while intentos_restantes > 0 and '_' in letras_adivinadas:
    ahorcado(intentos_usados, max_intentos)
    print("\nPalabra:", ' '.join(letras_adivinadas))
    print("Intentos restantes:", intentos_restantes)

    
    if letras_usadas:
        copia_letras = letras_usadas.copy()
        print("Letras usadas:", ' '.join(ordenamiento_burbuja(copia_letras)))

    letra = input("Ingresa una letra: ").lower().strip()

    letras_usadas.append(letra)

    encontrada = False

    for i in range(len(letras_palabra)):
        if letras_palabra[i] == letra:
            letras_adivinadas[i] = letra
            encontrada = True

    if encontrada:
        print(" La letra está en la palabra.")
    else:
        intentos_restantes -= 1
        intentos_usados += 1
        print(" La letra no está. Pierdes un intento.")


ahorcado(intentos_usados, max_intentos)
if '_' not in letras_adivinadas:
    print("\n ¡Ganaste! La palabra era:", palabra)
else:
    print("\n ¡Perdiste! La palabra era:", palabra)



