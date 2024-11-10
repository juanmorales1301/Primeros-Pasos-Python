"""
Este script demuestra el uso de algunos de los módulos más utilizados en Python con ejemplos prácticos.
"""

# 1. MÓDULO MATH
# El módulo math proporciona funciones matemáticas como trigonometría, exponenciales, logaritmos y más.

import math

# Ejemplo: Calcular la raíz cuadrada y el seno de un número
numero = 16
raiz_cuadrada = math.sqrt(numero)
seno = math.sin(math.radians(90))  # Convierte 90 grados a radianes y calcula el seno
print(f"Raíz cuadrada de {numero}: {raiz_cuadrada}, Seno de 90 grados: {seno}")
# Salida: Raíz cuadrada de 16: 4.0, Seno de 90 grados: 1.0


# 2. MÓDULO RANDOM
# El módulo random se utiliza para generar números aleatorios y hacer selecciones aleatorias.

import random

# Ejemplo: Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")
# Salida: Número aleatorio entre 1 y 10: <número>

# Ejemplo: Seleccionar un elemento aleatorio de una lista
colores = ["rojo", "verde", "azul"]
color_aleatorio = random.choice(colores)
print(f"Color aleatorio: {color_aleatorio}")
# Salida: Color aleatorio: <color>


# 3. MÓDULO DATETIME
# El módulo datetime se utiliza para trabajar con fechas y horas.

from datetime import datetime

# Ejemplo: Obtener la fecha y hora actual
fecha_actual = datetime.now()
print(f"Fecha y hora actual: {fecha_actual}")
# Salida: Fecha y hora actual: <fecha y hora>

# Ejemplo: Formatear una fecha
fecha_formateada = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha formateada: {fecha_formateada}")
# Salida: Fecha formateada: <día/mes/año hora:minutos:segundos>


# 4. MÓDULO OS
# El módulo os proporciona funciones para interactuar con el sistema operativo.

import os

# Ejemplo: Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")
# Salida: Directorio actual: <directorio>

# Ejemplo: Listar archivos en un directorio
archivos = os.listdir()
print(f"Archivos en el directorio actual: {archivos}")
# Salida: Archivos en el directorio actual: <lista de archivos>


# 5. MÓDULO SYS
# El módulo sys proporciona funciones para interactuar con el intérprete de Python y el sistema.

import sys

# Ejemplo: Obtener la versión de Python en uso
version_python = sys.version
print(f"Versión de Python: {version_python}")
# Salida: Versión de Python: <versión de Python>

# Ejemplo: Obtener los argumentos pasados a la línea de comandos
argumentos = sys.argv
print(f"Argumentos de la línea de comandos: {argumentos}")
# Salida: Argumentos de la línea de comandos: <lista de argumentos>


# 6. MÓDULO JSON
# El módulo json permite trabajar con datos en formato JSON (JavaScript Object Notation).

import json

# Ejemplo: Convertir un diccionario a una cadena JSON
datos = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}
datos_json = json.dumps(datos)
print(f"Datos en formato JSON: {datos_json}")
# Salida: Datos en formato JSON: {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}

# Ejemplo: Convertir una cadena JSON a un diccionario
datos_convertidos = json.loads(datos_json)
print(f"Datos convertidos de JSON: {datos_convertidos}")
# Salida: Datos convertidos de JSON: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}


# 7. MÓDULO TIME
# El módulo time permite trabajar con funciones relacionadas con el tiempo y la temporización.

import time

# Ejemplo: Pausar la ejecución del programa durante 2 segundos
print("Pausa de 2 segundos...")
time.sleep(2)
print("Continuación del programa.")
# Salida: (El programa se pausa durante 2 segundos)

# Ejemplo: Obtener el tiempo actual en segundos desde la época (1 de enero de 1970)
tiempo_actual = time.time()
print(f"Tiempo actual en segundos desde la época: {tiempo_actual}")
# Salida: Tiempo actual en segundos desde la época: <número de segundos>


# 8. MÓDULO STATISTICS
# El módulo statistics permite calcular estadísticas básicas como la media, mediana, moda, etc.

import statistics

# Ejemplo: Calcular la media de una lista de números
numeros = [10, 20, 30, 40, 50]
media = statistics.mean(numeros)
print(f"Media de los números: {media}")
# Salida: Media de los números: 30

# Ejemplo: Calcular la mediana de una lista de números
mediana = statistics.median(numeros)
print(f"Mediana de los números: {mediana}")
# Salida: Mediana de los números: 30


# 9. MÓDULO COLLECTIONS
# El módulo collections proporciona tipos de datos especializados, como namedtuple, deque, Counter, etc.

from collections import Counter

# Ejemplo: Contar la frecuencia de elementos en una lista
colores = ["rojo", "azul", "rojo", "verde", "azul", "rojo"]
contador_colores = Counter(colores)
print(f"Frecuencia de colores: {contador_colores}")
# Salida: Frecuencia de colores: Counter({'rojo': 3, 'azul': 2, 'verde': 1})


# 10. MÓDULO RE (EXPRESIONES REGULARES)
# El módulo re permite trabajar con expresiones regulares para buscar patrones en cadenas de texto.

import re

# Ejemplo: Buscar todas las palabras que comiencen con "P" en una cadena de texto
texto = "Python es un lenguaje de programación popular."
patron = r'P\w+'
coincidencias = re.findall(patron, texto)
print(f"Palabras que comienzan con 'P': {coincidencias}")
# Salida: Palabras que comienzan con 'P': ['Python', 'programación', 'popular']

