
# Alineación Múltiple de Secuencias

Proyecto realizado para la materia de Análisis y Modelación de Sistemas en el periodo Ene-24 a Ago-24 impartida por el Dr. Ernesto Rios Willars.
El programa busca realizar un alineamiento aplicando métodos de mutación de matrices con gaps, evaluación de las secuencias y cruzamiento entre éstas mismas.


## Authors

- [@GerardoCasten3](https://www.github.com/GerardoCasten3)


## Documentation
Dentro de la carpeta de Proyecto Final, podemos encontrar dos archivos. El corazón de nuestro programa se encuentra en "metodos_algoritmo.py" y nos encontraremos con los siguientes métodos:

imprimir_matriz(matriz):
Descripción: Este método imprime la matriz de palabras en el formato adecuado para visualizarla en la consola o en un archivo de texto.
Parámetros:
matriz: Una tupla de palabras que representa la matriz a imprimir.
Retorno: No retorna ningún valor, solo imprime la matriz en la consola.

mutar_matriz(matriz, tasa_mutacion):
Descripción: Realiza mutaciones en la matriz de palabras con una cierta tasa de mutación, introduciendo o eliminando letras aleatoriamente.
Parámetros:
matriz: La matriz de palabras a mutar.
tasa_mutacion: La probabilidad de que ocurra una mutación en una palabra.
Retorno: La matriz mutada después de aplicar las mutaciones.

evaluar_matriz(matriz):
Descripción: Evalúa la matriz de palabras asignando un puntaje basado en ciertos criterios, como la cantidad de letras correctas y la presencia de gaps ('-').
Parámetros:
matriz: La matriz de palabras a evaluar.
Retorno: El puntaje total de la matriz, que indica qué tan bien se ajusta a la solución deseada.

seleccionar_padres(poblacion, tam_torneo):
Descripción: Selecciona dos padres de una población utilizando el método del torneo, donde se eligen aleatoriamente varios individuos y se selecciona el mejor de ellos como padre.
Parámetros:
poblacion: La población de individuos a partir de los cuales seleccionar los padres.
tam_torneo: El tamaño del torneo a realizar, es decir, cuántos individuos se seleccionan aleatoriamente para cada torneo.
Retorno: Una lista de dos tuplas, cada una representando a un padre seleccionado y su puntaje asociado.

seleccionar_partes_comunes(matriz1, matriz2):
Descripción: Selecciona las partes comunes entre dos matrices de palabras, es decir, identifica las letras que coinciden en las mismas posiciones en ambas matrices.
Parámetros:
matriz1, matriz2: Las dos matrices de palabras a comparar.
Retorno: Una tupla con las partes comunes entre las dos matrices, representadas con letras y guiones ('-') que indican las diferencias.

cruzar_matrices(matriz1, matriz2, palabras_originales):
Descripción: Cruza dos matrices de palabras para producir un hijo, combinando las partes comunes de los padres y seleccionando letras aleatorias para las partes divergentes.
Parámetros:
matriz1, matriz2: Las matrices de palabras a cruzar.
palabras_originales: Las palabras originales, necesarias para asegurar que el hijo mantenga la misma longitud que el original.
Retorno: La matriz resultante del cruce, que representa a un nuevo individuo en la población.

busqueda_lineal(lista_tuplas):
Descripción: Realiza una búsqueda lineal en una lista de tuplas para encontrar el índice y el puntaje del mejor individuo.
Parámetros:
lista_tuplas: Una lista de tuplas donde cada tupla contiene un individuo y su puntaje.
Retorno: El índice y el puntaje del mejor individuo encontrados en la lista.

Para ejecutar el programa utilizaremos el archivo por nombre "proyecto_final.py". Podremos ajustar parámetros a nuestra conveniencia.

