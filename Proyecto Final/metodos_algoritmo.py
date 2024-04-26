# Autor: Jesús Gerardo Castillo Enríquez
import random

def imprimir_matriz(matriz):
    for palabra in matriz:
        print(palabra)
    print()

def mutar_matriz(matriz, tasa_mutacion):
    matriz_mutada = list(matriz)
    for i in range(len(matriz_mutada)):
        if random.random() < tasa_mutacion:
            palabra = list(matriz_mutada[i])
            gap_positions = [pos for pos, char in enumerate(palabra) if char == '-']  # Obtenemos las posiciones de los gaps
            num_gaps = len(gap_positions)
            if num_gaps < len(palabra) - 1:  # Verificar que no haya un guion en cada posicion
                for _ in range(3):  #Intenamos insertar hasta 3 giones por palabra
                    posicion = random.randint(0, len(palabra))
                    if posicion not in gap_positions:  # Evitar insertar un guion en una posición que ya tiene uno
                        palabra.insert(posicion, '-')
                        gap_positions.append(posicion)
            matriz_mutada[i] = ''.join(palabra)
    return tuple(matriz_mutada)

def evaluar_matriz(matriz):
    puntaje = 0
    for letras in zip(*matriz):
        letras_sin_gaps = [letra for letra in letras if letra != '-']
        if len(set(letras_sin_gaps)) == 1 and len(letras_sin_gaps) == len(matriz): # Si todas las letras son iguales y no hay gaps en la misma posición +2
            puntaje += 2
        elif '-' in letras:
            puntaje -= 0.5  # Si hay un gap en alguna de las palabras -0.5
        else:
            puntaje += 1  # Si no hay gaps y las letras no son iguales +0.5
    return puntaje

def seleccionar_padres(poblacion, tam_torneo):
    padres = []
    for _ in range(2):  # Seleccionamos 2 padres
        torneo = random.sample(poblacion, tam_torneo)
        ganador = max(torneo, key=lambda x: x[1])  # Seleccionamos al individuo con el mejor puntaje
        padres.append(ganador)
    return padres

def seleccionar_partes_comunes(matriz1, matriz2):
    partes_comunes = []
    for palabra_padre1, palabra_padre2 in zip(matriz1, matriz2):
        partes = []
        for letra_padre1, letra_padre2 in zip(palabra_padre1, palabra_padre2):
            if letra_padre1 == letra_padre2:
                partes.append(letra_padre1)
            else:
                partes.append('-')  # Marcar las diferencias con un guion
        partes_comunes.append(''.join(partes))
    
    # Mantener el orden de las letras
    for i in range(len(partes_comunes)):
        palabra_padre1, palabra_padre2 = matriz1[i], matriz2[i]
        palabra_comun = partes_comunes[i]
        nueva_palabra_comun = ''
        for letra_padre1, letra_padre2, letra_comun in zip(palabra_padre1, palabra_padre2, palabra_comun):
            if letra_comun != '-':
                nueva_palabra_comun += letra_comun
            elif letra_padre1 != '-':
                nueva_palabra_comun += letra_padre1
            else:
                nueva_palabra_comun += letra_padre2
        partes_comunes[i] = nueva_palabra_comun

    return tuple(partes_comunes)

def cruzar_matrices(matriz1, matriz2, palabras_originales):
    # Ajustar las matrices padres para que tengan la misma longitud que las palabras originales
    longitud_palabras = len(palabras_originales)
    if len(matriz1) < longitud_palabras:
        matriz1 += ('',) * (longitud_palabras - len(matriz1))
    if len(matriz2) < longitud_palabras:
        matriz2 += ('',) * (longitud_palabras - len(matriz2))

    partes_comunes = seleccionar_partes_comunes(matriz1, matriz2)
    hijo = []
    for palabra_partes, palabra_original in zip(partes_comunes, palabras_originales):
        palabra_hijo = ''
        indices_cruza = [i for i, parte in enumerate(palabra_partes) if parte == '-']
        for i, letra_original in enumerate(palabra_original):
            if i in indices_cruza:
                # Si la posición ya contiene una letra válida, mantener esa letra en lugar de seleccionar una del padre
                if palabra_hijo and palabra_hijo[-1] != '-':
                    palabra_hijo += palabra_hijo[-1]
                else:
                    # Asegurarnos de que el índice i esté dentro del rango de la longitud de la matriz padre
                    padre = matriz1 if random.random() < 0.5 else matriz2
                    if i < len(padre):
                        palabra_hijo += padre[i]
                    else:
                        palabra_hijo += '-'  # Si el índice está fuera de rango, añadimos un guion
            else:
                palabra_hijo += letra_original
        hijo.append(palabra_hijo)
    return tuple(hijo)

def busqueda_lineal(lista_tuplas):
    mejor_puntaje = float('-inf')  # Inicializamos el mejor puntaje como el menor número posible
    mejor_indice = -1

    for i, (_, puntaje) in enumerate(lista_tuplas):
        if puntaje >= mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_indice = i

    return mejor_indice, mejor_puntaje