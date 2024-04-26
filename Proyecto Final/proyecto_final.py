# Autor: Jesús Gerardo Castillo Enríquez
from metodos_algoritmo import evaluar_matriz, seleccionar_padres, cruzar_matrices, mutar_matriz, imprimir_matriz, busqueda_lineal

# Parámetros
num_generaciones = 85
tam_poblacion = 5
tasa_mutacion = 0.69
tam_torneo = 3

# Solicitar palabras al usuario
num_palabras = int(input("Ingrese el número de palabras para la matriz inicial: "))
palabras = []
for i in range(num_palabras):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.append(palabra)

# Matriz inicial
matriz_inicial = tuple(palabras)

# Inicializar población
poblacion = [(mutar_matriz(matriz_inicial, tasa_mutacion), 0) for _ in range(tam_poblacion)]  # Inicializamos los puntajes en 0

# Ciclo de generaciones
for generacion in range(1, num_generaciones + 1):
    print('------------- GENERACIÓN', generacion, '-------------')

    # Evaluar la población
    for i in range(len(poblacion)):
        poblacion[i] = (poblacion[i][0], evaluar_matriz(poblacion[i][0]))  # Actualizamos los puntajes

    # Seleccionar padres
    padres = seleccionar_padres(poblacion, tam_torneo)
    print("Padres seleccionados:", padres[0][0], "y", padres[1][0])

    # Cruzar los padres para generar hijos
    hijo1 = cruzar_matrices(padres[0][0], padres[1][0], palabras)
    hijo2 = cruzar_matrices(padres[1][0], padres[0][0], palabras)

    # Mutar los hijos
    hijo1_mutado = mutar_matriz(hijo1, tasa_mutacion)
    hijo2_mutado = mutar_matriz(hijo2, tasa_mutacion)

    # Calcular los puntajes de los hijos mutados
    puntaje_hijo1 = evaluar_matriz(hijo1_mutado)
    puntaje_hijo2 = evaluar_matriz(hijo2_mutado)

    # Crear las tuplas con los hijos mutados y sus puntajes
    hijo1_mutado = (hijo1_mutado, puntaje_hijo1)
    hijo2_mutado = (hijo2_mutado, puntaje_hijo2)

    # Extendemos la población y reemplazamos las peores matrices de la población 
    poblacion.extend([hijo1_mutado, hijo2_mutado])
    # Encontrar los dos peores puntajes
    peor1 = min(poblacion, key=lambda x: x[1])
    poblacion.remove(peor1)

    # Imprimir la población y sus puntajes
    print("Población y sus puntajes:")
    for i, (matriz, puntaje) in enumerate(poblacion, start=1):
        print("Matriz", i, ":")
        imprimir_matriz(matriz)
        print("Puntaje:", puntaje, '\n')


poblacion_final = poblacion
mejor_indice, mejor_puntaje = busqueda_lineal(poblacion_final)
print("La mejor matriz después de", num_generaciones, "generaciones es la:", mejor_indice + 1)
print("Con puntaje:", mejor_puntaje)
