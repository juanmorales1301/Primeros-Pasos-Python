# DEFINICIÓN DE SET (CONJUNTO)

# Un set es una colección desordenada y no indexada de elementos únicos.
# Los sets no permiten elementos duplicados y son mutables (pueden cambiar), aunque los elementos dentro de un set deben ser inmutables (como enteros, cadenas o tuplas).
# Los sets son útiles cuando se necesita garantizar que los elementos no se repitan o para realizar operaciones matemáticas de conjuntos (unión, intersección, etc.).

# CREACIÓN DE SETS

# Set de enteros
set_enteros = {1, 2, 3, 4, 5}
print("Set de enteros:", set_enteros)  # Salida: {1, 2, 3, 4, 5}

# Set con cadenas de texto
set_cadenas = {"uno", "dos", "tres", "cuatro"}
print("Set de cadenas:", set_cadenas)  # Salida: {'uno', 'dos', 'tres', 'cuatro'}

# Set con elementos mixtos
set_mixto = {1, "dos", 3.0, True}
print("Set mixto:", set_mixto)  # Salida: {1, 3.0, 'dos'}

# Set vacío (debe crearse usando set())
set_vacio = set()
print("Set vacío:", set_vacio)  # Salida: set()

# Agregar elementos a un set

# add(): Añade un elemento al set
set_enteros.add(6)
print("Set después de añadir un elemento:", set_enteros)  # Salida: {1, 2, 3, 4, 5, 6}

# update(): Añade múltiples elementos al set
set_enteros.update([7, 8, 9])
print("Set después de update:", set_enteros)  # Salida: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Remover elementos de un set

# remove(): Elimina un elemento específico, si no existe lanza un KeyError
set_enteros.remove(9)
print("Set después de remove:", set_enteros)  # Salida: {1, 2, 3, 4, 5, 6, 7, 8}

# discard(): Elimina un elemento, pero no lanza error si no existe
set_enteros.discard(10)  # No lanza error aunque 10 no esté en el set
print("Set después de discard (sin cambios):", set_enteros)  # Salida: {1, 2, 3, 4, 5, 6, 7, 8}

# pop(): Elimina y devuelve un elemento arbitrario del set
elemento_eliminado = set_enteros.pop()
print("Elemento eliminado:", elemento_eliminado)
print("Set después de pop:", set_enteros)

# clear(): Vacía completamente el set
set_enteros.clear()
print("Set después de clear:", set_enteros)  # Salida: set()

# OPERACIONES DE CONJUNTOS

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Unión de sets (une todos los elementos de ambos sets)
set_union = set_a.union(set_b)
print("Unión de set_a y set_b:", set_union)  # Salida: {1, 2, 3, 4, 5, 6}

# Intersección de sets (elementos comunes entre ambos sets)
set_interseccion = set_a.intersection(set_b)
print("Intersección de set_a y set_b:", set_interseccion)  # Salida: {3, 4}

# Diferencia entre sets (elementos en set_a que no están en set_b)
set_diferencia = set_a.difference(set_b)
print("Diferencia entre set_a y set_b:", set_diferencia)  # Salida: {1, 2}

# Diferencia simétrica (elementos que están en un set o en el otro, pero no en ambos)
set_dif_simetrica = set_a.symmetric_difference(set_b)
print("Diferencia simétrica entre set_a y set_b:", set_dif_simetrica)  # Salida: {1, 2, 5, 6}

# MÉTODOS COMUNES DE LOS SETS

# len(): Devuelve el número de elementos en el set
print("Tamaño de set_a:", len(set_a))  # Salida: 4

# in: Verifica si un elemento está en el set
print("¿Está 3 en set_a?", 3 in set_a)  # Salida: True

# isdisjoint(): Verifica si dos sets no tienen elementos en común
print("¿Son set_a y set_b disjuntos?", set_a.isdisjoint(set_b))  # Salida: False

# issubset(): Verifica si un set es subconjunto de otro
set_c = {1, 2}
print("¿Es set_c un subconjunto de set_a?", set_c.issubset(set_a))  # Salida: True

# issuperset(): Verifica si un set es superconjunto de otro
print("¿Es set_a un superconjunto de set_c?", set_a.issuperset(set_c))  # Salida: True

# Copiar un set
set_copia = set_a.copy()
print("Copia de set_a:", set_copia)  # Salida: {1, 2, 3, 4}

