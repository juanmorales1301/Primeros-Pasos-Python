# DEFINICIÓN DE SET (CONJUNTO)

# Una lista es una estructura de datos mutable en Python que puede almacenar una secuencia de elementos. 
# Al igual que las tuplas, los elementos dentro de una lista pueden ser de diferentes tipos. 
# Sin embargo, a diferencia de las tuplas, las listas son mutables, lo que significa que 
# sus elementos pueden ser modificados, añadidos o eliminados después de su creación. 
# Las listas se definen utilizando corchetes [].


# Tipos de datos en listas

# Lista de enteros
lista_enteros = [1, 2, 3, 4, 5]
print("Lista de enteros:", lista_enteros)  # Salida: [1, 2, 3, 4, 5]

# Lista de flotantes
lista_flotantes = [1.1, 2.2, 3.3, 4.4, 5.5]
print("Lista de flotantes:", lista_flotantes)  # Salida: [1.1, 2.2, 3.3, 4.4, 5.5]

# Lista de cadenas de texto
lista_cadenas = ["uno", "dos", "tres", "cuatro", "cinco"]
print("Lista de cadenas:", lista_cadenas)  # Salida: ['uno', 'dos', 'tres', 'cuatro', 'cinco']

# Lista de booleanos
lista_booleanos = [True, False, True, False]
print("Lista de booleanos:", lista_booleanos)  # Salida: [True, False, True, False]

# Lista de diferentes tipos de datos
lista_mixta = [1, "dos", 3.0, True]
print("Lista mixta:", lista_mixta)  # Salida: [1, 'dos', 3.0, True]

# Sublistas y listas anidadas

# Lista que contiene otras listas (listas anidadas)
lista_anidada = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print("Lista anidada:", lista_anidada)  # Salida: [[1, 2, 3], ['a', 'b', 'c'], [True, False]]

# Accediendo a sublistas y elementos dentro de sublistas
print("Primera sublista:", lista_anidada[0])  # Salida: [1, 2, 3]
print("Primer elemento de la primera sublista:", lista_anidada[0][0])  # Salida: 1

# Modificando elementos dentro de una sublista
lista_anidada[1][1] = "beta"
print("Lista anidada modificada:", lista_anidada)  # Salida: [[1, 2, 3], ['a', 'beta', 'c'], [True, False]]

# Combinaciones de listas

# Lista de listas que contiene enteros, cadenas y booleanos
lista_combinada = [[1, 2], ["tres", "cuatro"], [True, False]]
print("Lista combinada:", lista_combinada)  # Salida: [[1, 2], ['tres', 'cuatro'], [True, False]]

# Combinación de listas con diferentes tipos de datos
lista_varios_tipos = [[1, 2.5], ["cadena1", False], [3, True]]
print("Lista con varios tipos de datos:", lista_varios_tipos)  # Salida: [[1, 2.5], ['cadena1', False], [3, True]]

# Listas dentro de listas con diferentes tipos de operaciones
lista_operaciones = [[1 + 1, 2 * 2], ["cadena".upper(), False or True], [3.5 // 1, not True]]
print("Lista de operaciones con diferentes tipos:", lista_operaciones)  # Salida: [[2, 4], ['CADENA', True], [3.0, False]]

# Acceso a sublistas y modificación de elementos

# Modificando una lista dentro de una lista
lista_combinada[0].append(3)
print("Lista combinada después de modificar:", lista_combinada)  # Salida: [[1, 2, 3], ['tres', 'cuatro'], [True, False]]

# Ejemplo de lista de listas dentro de otra lista
lista_muy_anidada = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("Lista muy anidada:", lista_muy_anidada)  # Salida: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Accediendo a elementos dentro de listas anidadas
print("Accediendo a 6:", lista_muy_anidada[1][0][1])  # Salida: 6

# Usando list comprehensions con sublistas
lista_cuadrados = [[x**2 for x in sublista] for sublista in [[1, 2], [3, 4], [5, 6]]]
print("Cuadrados de elementos en sublistas:", lista_cuadrados)  # Salida: [[1, 4], [9, 16], [25, 36]]

# Combinación de sublistas, cadenas y operaciones
lista_mixta_combinada = [[True and False, "texto".capitalize()], [5.5 + 2.3, len("cadena")]]
print("Lista mixta combinada:", lista_mixta_combinada)  # Salida: [[False, 'Texto'], [7.8, 6]]


# MÉTODOS AVANZADOS PARA LISTAS

# sort(): Ordena la lista en orden ascendente
mi_lista = [4, 2, 9, 1]
mi_lista.sort()
print("Lista ordenada:", mi_lista)  # Salida: [1, 2, 4, 9]

# sort(reverse=True): Ordena la lista en orden descendente
mi_lista.sort(reverse=True)
print("Lista ordenada en orden descendente:", mi_lista)  # Salida: [9, 4, 2, 1]

# reverse(): Invierte el orden de los elementos de la lista
mi_lista.reverse()
print("Lista invertida:", mi_lista)  # Salida: [1, 2, 4, 9]

# copy(): Crea una copia de la lista
copia_lista = mi_lista.copy()
print("Copia de la lista:", copia_lista)  # Salida: [1, 2, 4, 9]

# count(): Devuelve el número de veces que un valor aparece en la lista
conteo = mi_lista.count(2)
print("El número 2 aparece:", conteo, "veces")  # Salida: 1

# index(): Devuelve el índice de la primera aparición de un valor
indice = mi_lista.index(4)
print("El índice de 4 es:", indice)  # Salida: 2

# clear(): Vacía la lista completamente
mi_lista.clear()
print("Lista después de clear:", mi_lista)  # Salida: []

# extend(): Añade múltiples elementos al final de la lista
mi_lista = [1, 2, 3]
mi_lista.extend([4, 5, 6])
print("Lista después de extend:", mi_lista)  # Salida: [1, 2, 3, 4, 5, 6]

# append(): Añade un elemento al final de la lista
mi_lista.append(7)
print("Lista después de append:", mi_lista)  # Salida: [1, 2, 3, 4, 5, 6, 7]

# insert(): Inserta un elemento en una posición específica
mi_lista.insert(3, 99)
print("Lista después de insert:", mi_lista)  # Salida: [1, 2, 3, 99, 4, 5, 6, 7]

# remove(): Elimina la primera aparición de un valor
mi_lista.remove(99)
print("Lista después de remove:", mi_lista)  # Salida: [1, 2, 3, 4, 5, 6, 7]

# pop(): Elimina y devuelve el último elemento de la lista
ultimo_elemento = mi_lista.pop()
print("Elemento eliminado:", ultimo_elemento)  # Salida: 7
print("Lista después de pop:", mi_lista)  # Salida: [1, 2, 3, 4, 5, 6]

# pop(index): Elimina y devuelve el elemento en la posición dada
elemento_en_index = mi_lista.pop(2)
print("Elemento en índice 2 eliminado:", elemento_en_index)  # Salida: 3
print("Lista después de pop(index):", mi_lista)  # Salida: [1, 2, 4, 5, 6]

