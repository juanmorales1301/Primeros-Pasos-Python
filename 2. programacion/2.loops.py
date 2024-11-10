# BUCLE FOR

# El bucle "for" en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena o rango de números).
# En cada iteración, la variable de bucle toma el siguiente valor de la secuencia.

# Iterar sobre una lista
mi_lista = [1, 2, 3, 4, 5]
for numero in mi_lista:
    print("Número:", numero)
# Salida: 
# Número: 1
# Número: 2
# Número: 3
# Número: 4
# Número: 5

# Iterar sobre una cadena de texto
mi_cadena = "Python"
for letra in mi_cadena:
    print("Letra:", letra)
# Salida: 
# Letra: P
# Letra: y
# Letra: t
# Letra: h
# Letra: o
# Letra: n

# Iterar sobre un rango de números
for i in range(5):
    print("i:", i)
# Salida: 0, 1, 2, 3, 4

# BUCLE WHILE

# El bucle "while" se ejecuta mientras una condición sea verdadera.

contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
# Salida: 0, 1, 2, 3, 4

# CONTROL DE FLUJO EN LOS BUCLES

# break: Se utiliza para salir de un bucle antes de que termine.

for i in range(10):
    if i == 5:
        break  # Se detiene cuando i es igual a 5
    print(i)
# Salida: 0, 1, 2, 3, 4

# continue: Salta a la siguiente iteración del bucle, omitiendo el código restante.

for i in range(5):
    if i == 3:
        continue  # Omite el valor 3
    print(i)
# Salida: 0, 1, 2, 4

# else en bucles: El bloque "else" se ejecuta cuando el bucle termina normalmente, es decir, sin que se haya ejecutado un "break".

for i in range(5):
    print(i)
else:
    print("El bucle ha terminado")
# Salida: 
# 0, 1, 2, 3, 4
# El bucle ha terminado

# BUCLES ANIDADOS

# Un bucle puede estar contenido dentro de otro bucle, lo que se conoce como bucles anidados.

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
# Salida:
# i: 0, j: 0
# i: 0, j: 1
# i: 1, j: 0
# i: 1, j: 1
# i: 2, j: 0
# i: 2, j: 1

# ITERANDO SOBRE UN DICCIONARIO

# Se puede utilizar un bucle "for" para iterar sobre las claves y valores de un diccionario.

mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
# Salida:
# Clave: nombre, Valor: Juan
# Clave: edad, Valor: 25
# Clave: ciudad, Valor: Bogotá

# USO DE WHILE CON CONDICIONES DINÁMICAS

# Se puede utilizar el bucle "while" para ejecutar operaciones mientras ciertas condiciones se mantengan.

saldo = 100
retiro = 20
while saldo > 0:
    print(f"Saldo actual: {saldo}")
    saldo -= retiro
# Salida:
# Saldo actual: 100
# Saldo actual: 80
# Saldo actual: 60
# Saldo actual: 40
# Saldo actual: 20

# FOR CON ENUMERATE()

# La función enumerate() devuelve tanto el índice como el valor durante la iteración.

colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"Índice: {indice}, Color: {color}")
# Salida:
# Índice: 0, Color: rojo
# Índice: 1, Color: verde
# Índice: 2, Color: azul

# WHILE INFINITO (USAR CON CUIDADO)

# Se puede crear un bucle infinito con while utilizando una condición siempre verdadera.
# Se debe tener cuidado de implementar una salida para evitar que el programa se cuelgue.

# while True:
#     respuesta = input("¿Deseas continuar? (s/n): ")
#     if respuesta == "n":
#         break

