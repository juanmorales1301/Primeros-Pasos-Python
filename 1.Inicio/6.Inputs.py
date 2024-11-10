
# Capturando un string del usuario
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")  # Salida: Hola, <nombre>!

# Capturando un número entero del usuario y convirtiéndolo (parseo) a int
edad = input("¿Cuántos años tienes? ")
edad_int = int(edad)
print("Tienes " + str(edad_int) + " años.")  # Salida: Tienes <edad> años.

# Capturando un número flotante y convirtiéndolo a float
altura = input("¿Cuánto mides en metros? ")
altura_float = float(altura)
print("Mides " + str(altura_float) + " metros.")  # Salida: Mides <altura> metros.

# Convertir una cadena en una lista usando split() y map()
numeros = input("Introduce tres números separados por comas: ")
numeros_lista = list(map(int, numeros.split(',')))
print("Lista de números:", numeros_lista)  # Salida: [<num1>, <num2>, <num3>]

# Capturando un valor booleano
respuesta = input("¿Te gusta programar? (sí/no): ")
respuesta_bool = respuesta.lower() in ['sí', 'si', 'yes', 'y']
print("Te gusta programar:", respuesta_bool)  # Salida: True/False

# Capturando varios datos en una sola línea y asignándolos a variables
nombre, edad = input("Introduce tu nombre y edad separados por un espacio: ").split()
edad = int(edad)  # Convertimos el segundo valor (edad) a int
print(f"Nombre: {nombre}, Edad: {edad}")  # Salida: Nombre: <nombre>, Edad: <edad>

# Capturando una lista de palabras y convirtiéndola en un set (eliminando duplicados)
palabras = input("Escribe varias palabras separadas por espacios: ")
palabras_set = set(palabras.split())
print("Set de palabras:", palabras_set)  # Salida: Set con palabras únicas

# Capturar y convertir a diferentes tipos en una línea usando map()
numeros = input("Introduce tres números decimales separados por espacios: ")
numeros_flotantes = list(map(float, numeros.split()))
print("Lista de números flotantes:", numeros_flotantes)  # Salida: [<num1>, <num2>, <num3>]

# Verificación de tipo
valor = input("Introduce un valor (puede ser número o texto): ")
if valor.isdigit():
    valor_int = int(valor)
    print(f"Has introducido un número entero: {valor_int}")
else:
    print(f"Has introducido texto: {valor}")

# Uso de try-except para manejar errores al convertir tipos
try:
    valor = int(input("Introduce un número entero: "))
    print(f"El número entero es: {valor}")
except ValueError:
    print("Error: No has introducido un número entero válido.")

# Convertir una entrada de fecha en un formato específico
fecha = input("Introduce una fecha en formato dd/mm/yyyy: ")
dia, mes, año = map(int, fecha.split('/'))
print(f"Día: {dia}, Mes: {mes}, Año: {año}")  # Salida: Día: <día>, Mes: <mes>, Año: <año>
