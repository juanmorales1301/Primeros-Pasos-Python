# DEFINICIÓN DE DICCIONARIO

# Un diccionario es una colección desordenada de pares clave-valor. Cada clave debe ser única e inmutable (como cadenas, números o tuplas), pero los valores pueden ser de cualquier tipo.
# Los diccionarios son mutables, es decir, sus elementos se pueden cambiar después de ser creados.

# CREACIÓN DE DICCIONARIOS

# Diccionario simple
diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Bogotá"
}
print("Diccionario:", diccionario)  # Salida: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}

# Diccionario vacío
diccionario_vacio = {}
print("Diccionario vacío:", diccionario_vacio)  # Salida: {}

# Crear diccionario usando el constructor dict()
diccionario2 = dict(nombre="Ana", edad=30, ciudad="Madrid")
print("Diccionario creado con dict():", diccionario2)  # Salida: {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Madrid'}

# Acceso a valores en el diccionario

# Acceder a un valor usando la clave
print("Nombre:", diccionario["nombre"])  # Salida: Juan

# Obtener un valor con get() (si no existe la clave, devuelve None o el valor por defecto especificado)
edad = diccionario.get("edad")
print("Edad:", edad)  # Salida: 25

# Intentar acceder a una clave inexistente con get(), devuelve None
print("Clave inexistente:", diccionario.get("profesion"))  # Salida: None

# AGREGAR Y MODIFICAR ELEMENTOS

# Añadir un nuevo par clave-valor
diccionario["profesion"] = "Ingeniero"
print("Diccionario después de añadir clave 'profesion':", diccionario)  # Salida: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá', 'profesion': 'Ingeniero'}

# Modificar un valor existente
diccionario["edad"] = 26
print("Diccionario después de modificar 'edad':", diccionario)  # Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Bogotá', 'profesion': 'Ingeniero'}

# ELIMINAR ELEMENTOS

# pop(): Elimina un par clave-valor y devuelve su valor
profesion_eliminada = diccionario.pop("profesion")
print("Profesión eliminada:", profesion_eliminada)  # Salida: Ingeniero
print("Diccionario después de pop:", diccionario)  # Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Bogotá'}

# popitem(): Elimina y devuelve el último par clave-valor añadido
ultimo_elemento = diccionario.popitem()
print("Último elemento eliminado:", ultimo_elemento)  # Salida: ('ciudad', 'Bogotá')
print("Diccionario después de popitem:", diccionario)  # Salida: {'nombre': 'Juan', 'edad': 26}

# clear(): Elimina todos los elementos del diccionario
diccionario.clear()
print("Diccionario después de clear:", diccionario)  # Salida: {}

# MÉTODOS COMUNES DE LOS DICCIONARIOS

# keys(): Devuelve todas las claves del diccionario
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}
print("Claves del diccionario:", diccionario.keys())  # Salida: dict_keys(['nombre', 'edad', 'ciudad'])

# values(): Devuelve todos los valores del diccionario
print("Valores del diccionario:", diccionario.values())  # Salida: dict_values(['Juan', 25, 'Bogotá'])

# items(): Devuelve todos los pares clave-valor como tuplas
print("Pares clave-valor:", diccionario.items())  # Salida: dict_items([('nombre', 'Juan'), ('edad', 25), ('ciudad', 'Bogotá')])

# Copiar un diccionario
copia_diccionario = diccionario.copy()
print("Copia del diccionario:", copia_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}

# COMBINACIÓN Y ACTUALIZACIÓN DE DICCIONARIOS

# update(): Actualiza el diccionario con pares clave-valor de otro diccionario o iterable
diccionario.update({"profesion": "Ingeniero", "edad": 26})
print("Diccionario después de update:", diccionario)  # Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Bogotá', 'profesion': 'Ingeniero'}

# fromkeys(): Crea un nuevo diccionario con claves dadas y un mismo valor para todas
claves = ["nombre", "edad", "ciudad"]
nuevo_diccionario = dict.fromkeys(claves, "Desconocido")
print("Diccionario creado con fromkeys:", nuevo_diccionario)  # Salida: {'nombre': 'Desconocido', 'edad': 'Desconocido', 'ciudad': 'Desconocido'}

# RECORRER DICCIONARIOS

# Recorrer claves y valores usando un bucle for
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
# Salida:
# Clave: nombre, Valor: Juan
# Clave: edad, Valor: 26
# Clave: ciudad, Valor: Bogotá
# Clave: profesion, Valor: Ingeniero

# Verificar si una clave existe en el diccionario
print("¿Existe la clave 'edad'?", "edad" in diccionario)  # Salida: True

