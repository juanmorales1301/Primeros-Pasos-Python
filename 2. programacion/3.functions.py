
# DEFINICIÓN DE UNA FUNCIÓN

# Las funciones se definen utilizando la palabra clave "def", seguida del nombre de la función y paréntesis ().
# El bloque de código dentro de la función se ejecuta cuando se llama a la función.

def saludo():
    print("Hola, mundo")

# Llamada a la función
saludo()  # Salida: Hola, mundo

# FUNCIÓN CON ARGUMENTOS

# Puedes pasar datos a una función como parámetros.
# Los parámetros son variables que se utilizan en la definición de la función.

def saludo_personalizado(nombre):
    print(f"Hola, {nombre}")

saludo_personalizado("Juan")  # Salida: Hola, Juan

# FUNCIÓN CON MÚLTIPLES PARÁMETROS

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(f"Resultado de la suma: {resultado}")  # Salida: Resultado de la suma: 8

# VALORES POR DEFECTO EN FUNCIONES

# Se pueden asignar valores por defecto a los parámetros de una función.
# Si no se pasa un argumento para un parámetro, se utilizará su valor por defecto.

def saludo_por_defecto(nombre="amigo"):
    print(f"Hola, {nombre}")

saludo_por_defecto()  # Salida: Hola, amigo
saludo_por_defecto("Ana")  # Salida: Hola, Ana

# FUNCIÓN CON RETORNO DE VALOR

# La palabra clave "return" se utiliza para devolver un valor desde una función.

def multiplicar(a, b):
    return a * b

producto = multiplicar(4, 5)
print(f"Producto: {producto}")  # Salida: Producto: 20

# FUNCIÓN CON ARGUMENTOS NOMBRADOS

# Los argumentos pueden ser pasados por nombre, lo que permite especificar qué valor corresponde a cada parámetro.

def restar(a, b):
    return a - b

resultado = restar(b=10, a=20)
print(f"Resultado de la resta: {resultado}")  # Salida: Resultado de la resta: 10

# FUNCIÓN CON NÚMERO INDEFINIDO DE ARGUMENTOS (*ARGS)

# Puedes utilizar *args para pasar un número indeterminado de argumentos a una función.
# Los argumentos se almacenan como una tupla.

def suma_indefinida(*args):
    return sum(args)

resultado = suma_indefinida(1, 2, 3, 4, 5)
print(f"Suma indefinida: {resultado}")  # Salida: Suma indefinida: 15

# FUNCIÓN CON NÚMERO INDEFINIDO DE ARGUMENTOS NOMBRADOS (**KWARGS)

# Puedes utilizar **kwargs para pasar un número indeterminado de argumentos nombrados a una función.
# Los argumentos se almacenan como un diccionario.

def imprimir_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_informacion(nombre="Juan", edad=25, ciudad="Bogotá")
# Salida:
# nombre: Juan
# edad: 25
# ciudad: Bogotá

# FUNCIONES LAMBDA (FUNCIONES ANÓNIMAS)

# Las funciones lambda son funciones anónimas, que pueden tener cualquier número de argumentos pero solo una expresión.
# Se utilizan en casos donde se requiere una función pequeña y simple.

doble = lambda x: x * 2
print(f"El doble de 5 es: {doble(5)}")  # Salida: El doble de 5 es: 10

# Lambda con múltiples argumentos
multiplicar = lambda x, y: x * y
print(f"Multiplicación de 3 y 4: {multiplicar(3, 4)}")  # Salida: Multiplicación de 3 y 4: 12

# FUNCIONES DENTRO DE OTRAS FUNCIONES

# Las funciones también se pueden definir dentro de otras funciones.

def funcion_externa():
    print("Esta es la función externa")
    
    def funcion_interna():
        print("Esta es la función interna")
    
    funcion_interna()

funcion_externa()
# Salida:
# Esta es la función externa
# Esta es la función interna

# FUNCIONES RECURSIVAS

# Una función recursiva es una función que se llama a sí misma.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial de 5: {factorial(5)}")  # Salida: Factorial de 5: 120

# FUNCIONES COMO ARGUMENTOS

# En Python, las funciones se pueden pasar como argumentos a otras funciones.

def aplicar_operacion(funcion, valor):
    return funcion(valor)

resultado = aplicar_operacion(doble, 10)
print(f"Resultado al aplicar operación: {resultado}")  # Salida: Resultado al aplicar operación: 20

