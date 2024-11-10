"""
Este script demuestra el uso de varios métodos de cadena en Python,
ordenados desde los más importantes y frecuentemente utilizados, 
hasta los menos comunes.
"""

# length of string (len() is commonly used)
cadena = "Hola Mundo"
print(len(cadena))  # Salida: 10

# lower(): Convierte la cadena a minúsculas
resultado = "HOLA".lower()
print(resultado)  # Salida: hola

# upper(): Convierte la cadena a mayúsculas
resultado = "hola".upper()
print(resultado)  # Salida: HOLA

# strip(): Elimina los espacios en blanco a ambos lados de la cadena
resultado = "  hola  ".strip()
print(resultado)  # Salida: 'hola'

# split(sep): Divide la cadena usando el separador especificado
resultado = "manzana, banana, cereza".split(', ')
print(resultado)  # Salida: ['manzana', 'banana', 'cereza']

# replace(old, new): Reemplaza las ocurrencias de un subcadena con otra subcadena
resultado = "hola mundo".replace("mundo", "amigos")
print(resultado)  # Salida: hola amigos

# join(iterable): Une elementos de un iterable con la cadena como separador
resultado = ", ".join(["manzana", "banana", "cereza"])
print(resultado)  # Salida: manzana, banana, cereza

# startswith(prefix): Verifica si la cadena comienza con el prefijo especificado
resultado = "hola".startswith('h')
print(resultado)  # Salida: True

# endswith(suffix): Verifica si la cadena termina con un sufijo específico
resultado = "hola".endswith('a')
print(resultado)  # Salida: True

# isdigit(): Verifica si la cadena contiene solo dígitos
resultado = "123".isdigit()
print(resultado)  # Salida: True

# isalpha(): Verifica si la cadena contiene solo caracteres alfabéticos
resultado = "hola".isalpha()
print(resultado)  # Salida: True

# isalnum(): Verifica si la cadena es alfanumérica
resultado = "hola123".isalnum()
print(resultado)  # Salida: True

# count(sub): Cuenta las ocurrencias de un subcadena en la cadena
resultado = "hola".count('l')
print(resultado)  # Salida: 1

# find(sub): Encuentra la primera ocurrencia de un subcadena
resultado = "hola".find('l')
print(resultado)  # Salida: 2

# rfind(sub): Encuentra la última ocurrencia de un subcadena
resultado = "hola".rfind('l')
print(resultado)  # Salida: 2

# partition(sep): Divide la cadena en tres partes: la parte antes del separador, el separador en sí, y la parte después
resultado = "hola mundo".partition(' ')
print(resultado)  # Salida: ('hola', ' ', 'mundo')

# capitalize(): Capitaliza el primer carácter de la cadena
resultado = "hola mundo".capitalize()
print(resultado)  # Salida: Hola mundo

# title(): Convierte la cadena a formato de título
resultado = "hola mundo".title()
print(resultado)  # Salida: Hola Mundo

# islower(): Verifica si todos los caracteres en la cadena son minúsculas
resultado = "hola".islower()
print(resultado)  # Salida: True

# isupper(): Verifica si todos los caracteres en la cadena son mayúsculas
resultado = "HOLA".isupper()
print(resultado)  # Salida: True

# lstrip(): Elimina los espacios en blanco a la izquierda de la cadena
resultado = "  hola".lstrip()
print(resultado)  # Salida: 'hola'

# rstrip(): Elimina los espacios en blanco a la derecha de la cadena
resultado = "hola   ".rstrip()
print(resultado)  # Salida: 'hola'

# swapcase(): Invierte el caso de todos los caracteres en la cadena
resultado = "Hola Mundo".swapcase()
print(resultado)  # Salida: hOLA mUNDO

# zfill(width): Añade ceros a la izquierda para rellenar la cadena hasta el ancho especificado
resultado = "42".zfill(5)
print(resultado)  # Salida: 00042

# __add__(self, value): Concatena dos cadenas
cadena1 = "Hola"
cadena2 = " Mundo"
resultado = cadena1.__add__(cadena2)
print(resultado)  # Salida: Hola Mundo

# __contains__(self, item): Verifica si una cadena contiene un subcadena
resultado = "ola" in cadena1
print(resultado)  # Salida: True

# __eq__(self, value): Verifica si dos cadenas son iguales
resultado = cadena1.__eq__("Hola")
print(resultado)  # Salida: True

# __getitem__(self, index): Devuelve el carácter en un índice específico
resultado = cadena1.__getitem__(1)
print(resultado)  # Salida: o

# __len__(self): Devuelve la longitud de la cadena
resultado = cadena1.__len__()
print(resultado)  # Salida: 4

# center(width): Centra la cadena dentro de un ancho especificado
resultado = "hola".center(10)
print(resultado)  # Salida: '  hola   '

# ljust(width): Justifica la cadena a la izquierda en un campo de un ancho dado
resultado = "hola".ljust(10)
print(resultado)  # Salida: 'hola      '

# rjust(width): Justifica la cadena a la derecha en un campo de un ancho dado
resultado = "hola".rjust(10)
print(resultado)  # Salida: '      hola'

# expandtabs(tabsize): Reemplaza las tabulaciones con espacios
resultado = "hola\tmundo".expandtabs(4)
print(resultado)  # Salida: hola    mundo

# rpartition(sep): Divide la cadena en tres partes, buscando desde la derecha
resultado = "hola mundo".rpartition(' ')
print(resultado)  # Salida: ('hola', ' ', 'mundo')

# format(*args, **kwargs): Formatea la cadena usando los argumentos dados
resultado = "Hola {}".format("Mundo")
print(resultado)  # Salida: Hola Mundo

# removeprefix(prefix): Elimina el prefijo dado de la cadena
resultado = "prefijo_hola".removeprefix("prefijo_")
print(resultado)  # Salida: hola

# removesuffix(suffix): Elimina el sufijo dado de la cadena
resultado = "hola_sufijo".removesuffix("_sufijo")
print(resultado)  # Salida: hola

# isidentifier(): Verifica si la cadena es un identificador válido en Python
resultado = "nombre_variable".isidentifier()
print(resultado)  # Salida: True

# isascii(): Verifica si la cadena contiene solo caracteres ASCII
resultado = "hola".isascii()
print(resultado)  # Salida: True

# isdigit(): Verifica si la cadena contiene solo caracteres numéricos
resultado = "123".isdigit()
print(resultado)  # Salida: True

# isspace(): Verifica si la cadena contiene solo espacios en blanco
resultado = "   ".isspace()
print(resultado)  # Salida: True

# isnumeric(): Verifica si la cadena contiene solo caracteres numéricos
resultado = "123".isnumeric()
print(resultado)  # Salida: True

# __ge__(self, value): Verifica si la cadena es mayor o igual que otra cadena
resultado = "manzana".__ge__("banana")
print(resultado)  # Salida: False

# __lt__(self, value): Verifica si la cadena es menor que otra cadena
resultado = "manzana".__lt__("banana")
print(resultado)  # Salida: True

# __mul__(self, value): Repite la cadena un número de veces
resultado = cadena1.__mul__(3)
print(resultado)  # Salida: HolaHolaHola

# __repr__(self): Devuelve una representación en cadena del objeto
resultado = cadena1.__repr__()
print(resultado)  # Salida: 'Hola'
