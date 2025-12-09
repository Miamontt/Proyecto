import random

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
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
# Elegimos la etapa según cuántos intentos ya se usaron
    idx = min(len(etapas)-1, intentos_usados)
    print(etapas[idx])

# Diccionario de palabras por dificultad (se puede ampliar)
palabras_por_dificultad = {
    "baja": ["listi", "gato", "casa", "perro"],
    "media": ["introducción", "programación", "computadora"],
    "alta": ["al pensamiento computacional", "python", "arquitectura"]
}

# Elegir dificultad
print("Elige la dificultad: baja / media / alta")
dificultad = input("Dificultad: ").lower()

# Configurar palabra (elegida aleatoriamente de la lista de la dificultad)
palabra = random.choice(palabras_por_dificultad[dificultad]).lower()
letras_palabra = list(palabra)
letras_adivinadas = ['_' if letra != ' ' else ' ' for letra in letras_palabra]

max_intentos = 6
intentos_restantes = max_intentos
intentos_usados = 0  # para mostrar etapas

letras_usadas = []

# Bucle principal del juego
while intentos_restantes > 0 and '_' in letras_adivinadas:
    mostrar_ahorcado(intentos_usados, max_intentos)
    print("\nPalabra:", ' '.join(letras_adivinadas))
    print("Intentos restantes:", intentos_restantes)

    # Mostrar letras usadas ordenadas (no modificar el original)
    if letras_usadas:
        copia_letras = letras_usadas.copy()
        print("Letras usadas:", ' '.join(ordenamiento_burbuja(copia_letras)))

    letra = input("Ingresa una letra: ").lower().strip()

        

    letras_usadas.append(letra)

    # Verificar si la letra está en la palabra (búsqueda simple)
    encontrada = False
    for i in range(len(letras_palabra)):
        if letras_palabra[i] == letra:
            letras_adivinadas[i] = letra
            encontrada = True

    if encontrada:
        print("La letra está en la palabra.")
    else:
        intentos_restantes -= 1
        intentos_usados += 1
        print("La letra no está.")

# Resultado final
ahorcado(intentos_usados, max_intentos)
if '_' not in letras_adivinadas:
    print("\n ganaste la palabra era:", palabra)
else:
    print("\n Perdiste la palabra era:", palabra)
