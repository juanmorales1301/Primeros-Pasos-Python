
# Operadores básicos

# Suma
resultado = 5 + 3
print("Suma:", resultado)  # Salida: 8

# Resta
resultado = 5 - 3
print("Resta:", resultado)  # Salida: 2

# Multiplicación
resultado = 5 * 3
print("Multiplicación:", resultado)  # Salida: 15

# División
resultado = 5 / 3
print("División:", resultado)  # Salida: 1.6666666666666667

# División entera (floor division)
resultado = 5 // 3
print("División entera:", resultado)  # Salida: 1

# Módulo (residuo de la división)
resultado = 5 % 3
print("Módulo:", resultado)  # Salida: 2

# Exponenciación
resultado = 5 ** 3
print("Exponenciación:", resultado)  # Salida: 125

# Operadores de comparación

# Mayor que
resultado = 5 > 3
print("5 > 3:", resultado)  # Salida: True

# Menor que
resultado = 5 < 3
print("5 < 3:", resultado)  # Salida: False

# Mayor o igual que
resultado = 5 >= 3
print("5 >= 3:", resultado)  # Salida: True

# Menor o igual que
resultado = 5 <= 3
print("5 <= 3:", resultado)  # Salida: False

# Igualdad
resultado = 5 == 3
print("5 == 3:", resultado)  # Salida: False

# Desigualdad
resultado = 5 != 3
print("5 != 3:", resultado)  # Salida: True

# Funciones numéricas comunes

# abs(): Devuelve el valor absoluto
resultado = abs(-5)
print("Valor absoluto:", resultado)  # Salida: 5

# pow(base, exp): Devuelve el resultado de elevar la base a la potencia del exponente
resultado = pow(2, 3)
print("Potencia:", resultado)  # Salida: 8

# round(): Redondea un número al entero más cercano o al número de decimales especificado
resultado = round(5.678, 2)
print("Redondear:", resultado)  # Salida: 5.68

# max(): Devuelve el mayor de los argumentos
resultado = max(5, 3, 10)
print("Máximo:", resultado)  # Salida: 10

# min(): Devuelve el menor de los argumentos
resultado = min(5, 3, 10)
print("Mínimo:", resultado)  # Salida: 3

# sum(): Suma todos los elementos de un iterable
resultado = sum([1, 2, 3, 4, 5])
print("Suma total:", resultado)  # Salida: 15

# divmod(): Devuelve el cociente y el resto de la división
resultado = divmod(5, 3)
print("Divmod (cociente, residuo):", resultado)  # Salida: (1, 2)

# Funciones matemáticas adicionales del módulo math
import math

# math.sqrt(): Raíz cuadrada
resultado = math.sqrt(16)
print("Raíz cuadrada:", resultado)  # Salida: 4.0

# math.floor(): Redondea hacia abajo
resultado = math.floor(5.678)
print("Redondear hacia abajo:", resultado)  # Salida: 5

# math.ceil(): Redondea hacia arriba
resultado = math.ceil(5.678)
print("Redondear hacia arriba:", resultado)  # Salida: 6

# math.log(): Logaritmo natural
resultado = math.log(10)
print("Logaritmo natural de 10:", resultado)  # Salida: 2.302585092994046

# math.log10(): Logaritmo en base 10
resultado = math.log10(100)
print("Logaritmo en base 10 de 100:", resultado)  # Salida: 2.0

# math.sin(), math.cos(), math.tan(): Funciones trigonométricas
resultado_sin = math.sin(math.pi / 2)  # Sin de 90 grados (π/2 radianes)
print("Seno de 90 grados:", resultado_sin)  # Salida: 1.0

resultado_cos = math.cos(0)  # Coseno de 0 grados
print("Coseno de 0 grados:", resultado_cos)  # Salida: 1.0

resultado_tan = math.tan(math.pi / 4)  # Tangente de 45 grados (π/4 radianes)
print("Tangente de 45 grados:", resultado_tan)  # Salida: 1.0

# math.factorial(): Factorial de un número
resultado = math.factorial(5)
print("Factorial de 5:", resultado)  # Salida: 120
