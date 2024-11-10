# IF SIMPLE

# La estructura básica de un condicional en Python es la siguiente:
# Si la condición es verdadera, ejecuta el bloque de código.

x = 10
if x > 5:
    print("x es mayor que 5")  # Salida: x es mayor que 5

# IF-ELSE

# Si la condición es verdadera, ejecuta el bloque de código dentro del "if".
# Si la condición es falsa, ejecuta el bloque de código dentro del "else".

x = 3
if x > 5:
    print("x es mayor que 5")
else:
    print("x es menor o igual que 5")  # Salida: x es menor o igual que 5

# IF-ELIF-ELSE

# Puedes usar "elif" (else if) para manejar múltiples condiciones.
# Si ninguna de las condiciones es verdadera, se ejecutará el bloque "else".

x = 5
if x > 10:
    print("x es mayor que 10")
elif x == 5:
    print("x es igual a 5")  # Salida: x es igual a 5
else:
    print("x es menor que 5")

# CONDICIONALES ANIDADOS

# Puedes anidar condicionales dentro de otros condicionales.

x = 8
if x > 5:
    print("x es mayor que 5")  # Salida: x es mayor que 5
    if x > 7:
        print("x es también mayor que 7")  # Salida: x es también mayor que 7

# OPERADOR TERNARIO

# El operador ternario es una manera de escribir condicionales de manera más concisa.

x = 10
resultado = "Mayor que 5" if x > 5 else "Menor o igual que 5"
print(resultado)  # Salida: Mayor que 5

# CONDICIONES MÚLTIPLES

# Puedes combinar varias condiciones usando "and" (y) y "or" (o).

x = 10
y = 20

# Ambas condiciones deben ser verdaderas para que el bloque se ejecute
if x > 5 and y > 15:
    print("x es mayor que 5 y y es mayor que 15")  # Salida: x es mayor que 5 y y es mayor que 15

# Al menos una condición debe ser verdadera para que el bloque se ejecute
if x > 15 or y > 15:
    print("Al menos una condición es verdadera")  # Salida: Al menos una condición es verdadera

# USO DE OPERADORES DE COMPARACIÓN

# ==: Verifica si dos valores son iguales
x = 5
if x == 5:
    print("x es igual a 5")  # Salida: x es igual a 5

# !=: Verifica si dos valores son diferentes
if x != 10:
    print("x no es igual a 10")  # Salida: x no es igual a 10

# >, >=, <, <=: Comparan si un valor es mayor, mayor o igual, menor, o menor o igual a otro valor

x = 8
if x >= 5:
    print("x es mayor o igual que 5")  # Salida: x es mayor o igual que 5

if x < 10:
    print("x es menor que 10")  # Salida: x es menor que 10

# EVALUACIÓN DE VALORES VERDADEROS O FALSOS (TRUTHY/FALSY)

# Python evalúa algunos valores como "falsos" (False) por defecto: 0, None, False, cadenas vacías, listas vacías, etc.
# Todo lo demás se considera "verdadero" (True).

valor = ""
if valor:
    print("Valor es verdadero")
else:
    print("Valor es falso")  # Salida: Valor es falso

# Bucle for con condicionales

# Los condicionales también se pueden usar dentro de bucles.
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"{numero} es par")  # Salida: 2, 4, 6, 8, 10 son pares

# USO DE CONDICIONALES EN FUNCIONES

# Los condicionales se pueden usar dentro de funciones para controlar el flujo de ejecución.

def verificar_numero(x):
    if x > 0:
        return "Número positivo"
    elif x < 0:
        return "Número negativo"
    else:
        return "El número es cero"

print(verificar_numero(10))  # Salida: Número positivo
print(verificar_numero(-5))  # Salida: Número negativo
print(verificar_numero(0))   # Salida: El número es cero

