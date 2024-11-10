# Maneras de generar cadenas de texto (Strings)
print("Hola mundo")
print('Hola mundo')
print('''Hola mundo''')
print("""Hola mundo""")

print(type("Hola mundo")) # Extrae el typo del elemento

print("Uniendo" + "Caracteres") # Concatena cadenas de texto

print(100+50) # Suma de numeros

#Numeros
print(100) # Integer
print(type(100))
print(3.12)  # Float
print(type(3.12))

# Booleanos
print(True)
print(type(True))
print(False)
print(type(False))


# Lista de datos, son lista de valores similares a las tuplas pero modificables, se pueden alterar los datos
print([10,38,20,39,4]) # Lista de enteros
print(["Hola", "Mundo"]) # Lista de strings
print(["Hola", 10, True, "Mundo", False, 495.2]) # Lista combinada
print(type([10,38,20,39,4]))
print([]) # Lista vacia


#Tuplas (No se pueden cambiar los datos, son contantes estaticas, inmutable), pero son mas rapidas y se accede a los datos mas rapido
print((10, 394, 30, 23))
print(type((10, 394, 30, 23)))
print(()) # Tupla vacia


#Diccionarios, agrupa datos que pertenecen a una misma entidad, similar a los objetos de POO con parametros o un objeto JSON
{
    "nombre": "Juan",
    "apellido": "Morales",
    "edad": 23
}

print(type({
    "nombre": "Juan",
    "apellido": "Morales",
    "edad": 23
}))



# Tipo no definido
print(None)
print(type(None))