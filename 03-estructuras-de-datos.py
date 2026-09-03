# clase de 31-08-2026


# Lista > Corchetes, separados por comas. Se accede por index. 
# Similar a un array en otros lenguajes. Se puede modificar, agregar y eliminar elementos.

usuarios = ["Alberto", "Berta", "Coc"]
# print(usuarios[0])

usuarios.append("Dani")

usuarios.sort(key=lambda x: len(x), reverse=True)


for usuario in usuarios:
    print("Procesando: ",usuario)   
    if usuario == "pepe":
        usuarios.remove(usuario)

# Tupla > Paréntesis, separados por comas. Se accede por index. 
# Similar a una lista, pero no se puede modificar, agregar o eliminar elementos.

coordenadas = (10, 20, [ 20, 30, 40])
coordenadas[2].append(50) # Si se pueden modificar sus elementos internos si estos son mutables (listas, diccionarios, etc).
print(coordenadas)

# DICCIONARIO > Llaves, separados por comas. Se accede por clave.
# Similar a un objeto en otros lenguajes. Se puede modificar, agregar y eliminar elementos

user = {
    "name": "Alberto",
    "lastname": "Gonzalez",
    "age": 30,
}
print(user.keys())
print(user.values())

# print(user["name"] + " " + user["lastname"])


# lista de diccionarios
users = [
    {"name": "Alberto", "lastname": "Gonzalez", "age": 30},
    {"name": "Berta", "lastname": "Martinez", "age": 25},
    {"name": "Coc", "lastname": "Lopez", "age": 35}
]

print(users)

