# DEFINICIÓN DE SET (CONJUNTO)

# Una tupla es una estructura de datos inmutable en Python que puede almacenar una
# secuencia de elementos. Los elementos dentro de una tupla pueden ser de diferentes tipos 
# (como enteros, cadenas, etc.). Una vez que una tupla es creada, sus elementos no pueden 
# ser modificados (es decir, es inmutable). Se utilizan comúnmente cuando se necesita una secuencia 
# de elementos que no debe cambiar a lo largo del tiempo. Las tuplas se definen utilizando paréntesis ().

# CREACIÓN DE TUPLAS

# Tupla de enteros
tupla_enteros = (1, 2, 3, 4, 5)
print("Tupla de enteros:", tupla_enteros)  # Salida: (1, 2, 3, 4, 5)

# Tupla de flotantes
tupla_flotantes = (1.1, 2.2, 3.3)
print("Tupla de flotantes:", tupla_flotantes)  # Salida: (1.1, 2.2, 3.3)

# Tupla de cadenas de texto
tupla_cadenas = ("uno", "dos", "tres")
print("Tupla de cadenas:", tupla_cadenas)  # Salida: ('uno', 'dos', 'tres')

# Tupla de diferentes tipos de datos
tupla_mixta = (1, "dos", 3.0, True)
print("Tupla mixta:", tupla_mixta)  # Salida: (1, 'dos', 3.0, True)

# Tuplas anidadas (tuplas dentro de tuplas)
tupla_anidada = ((1, 2), ("a", "b"), (True, False))
print("Tupla anidada:", tupla_anidada)  # Salida: ((1, 2), ('a', 'b'), (True, False))

# Tupla con un solo elemento (requiere una coma final para ser considerada tupla)
tupla_un_elemento = (1,)
print("Tupla con un solo elemento:", tupla_un_elemento)  # Salida: (1,)

# ACCESO A ELEMENTOS EN TUPLAS

# Accediendo a un elemento por su índice
primer_elemento = tupla_enteros[0]
print("Primer elemento de la tupla:", primer_elemento)  # Salida: 1

# Accediendo al último elemento usando índice negativo
ultimo_elemento = tupla_enteros[-1]
print("Último elemento de la tupla:", ultimo_elemento)  # Salida: 5

# Acceso a elementos en una tupla anidada
print("Elemento dentro de tupla anidada:", tupla_anidada[1][0])  # Salida: 'a'

# Rebanadas (slicing) en tuplas
sub_tupla = tupla_enteros[1:4]
print("Subtupla (índices 1 a 3):", sub_tupla)  # Salida: (2, 3, 4)

# OPERACIONES CON TUPLAS

# Concatenar dos tuplas
tupla_concatenada = tupla_enteros + tupla_flotantes
print("Tuplas concatenadas:", tupla_concatenada)  # Salida: (1, 2, 3, 4, 5, 1.1, 2.2, 3.3)

# Repetir una tupla (multiplicación)
tupla_repetida = tupla_enteros * 3
print("Tupla repetida:", tupla_repetida)  # Salida: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# MÉTODOS DISPONIBLES PARA TUPLAS

# count(): Cuenta cuántas veces aparece un valor en la tupla
conteo = tupla_enteros.count(3)
print("El número 3 aparece:", conteo, "veces")  # Salida: 1

# index(): Devuelve el índice de la primera aparición de un valor
indice = tupla_enteros.index(4)
print("El índice de 4 es:", indice)  # Salida: 3

# DESDE LISTA A TUPLA Y VICEVERSA

# Convertir una lista a una tupla
lista = [1, 2, 3, 4]
tupla_desde_lista = tuple(lista)
print("Tupla convertida desde lista:", tupla_desde_lista)  # Salida: (1, 2, 3, 4)

# Convertir una tupla a una lista
lista_desde_tupla = list(tupla_enteros)
print("Lista convertida desde tupla:", lista_desde_tupla)  # Salida: [1, 2, 3, 4, 5]

# DESEMPAQUETADO DE TUPLAS

# Asignar los valores de una tupla a múltiples variables (desempaquetado)
a, b, c = (1, 2, 3)
print("Valores desempaquetados:", a, b, c)  # Salida: 1 2 3

# Desempaquetado con el operador "*"
primero, *resto = tupla_enteros
print("Primero:", primero)  # Salida: 1
print("Resto:", resto)  # Salida: [2, 3, 4, 5]

# FUNCIONES ADICIONALES CON TUPLAS

# len(): Devuelve la longitud de la tupla
print("Longitud de la tupla:", len(tupla_enteros))  # Salida: 5

# max(): Devuelve el valor máximo de una tupla
print("Valor máximo en la tupla:", max(tupla_enteros))  # Salida: 5

# min(): Devuelve el valor mínimo de una tupla
print("Valor mínimo en la tupla:", min(tupla_enteros))  # Salida: 1

# sorted(): Ordena los elementos de la tupla y devuelve una lista
print("Tupla ordenada como lista:", sorted(tupla_enteros))  # Salida: [1, 2, 3, 4, 5]

# Verificar si un elemento está en la tupla (operador in)
print("¿2 está en la tupla?", 2 in tupla_enteros)  # Salida: True

# Immutabilidad de las tuplas
# Intentar modificar una tupla causará un error, ya que las tuplas son inmutables
# tupla_enteros[0] = 10  # Esto lanzaría un TypeError

