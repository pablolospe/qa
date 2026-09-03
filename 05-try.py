# clase de 31-08-2026

def trying():
    try:
        number = int(input("Ingrese un número: "))
        print("El número es: ", number)
    except ValueError:
        print("No se puede convertir a entero")

    finally:
        print("Fin del bloque try-except")


trying()


# try:
#     number = invalue except ValueError:
#     print("No se puede convertir a entero")


users = [
    {"name": "Alberto", "lastname": "Gonzalez", "age": 30},
    {"name": "Berta", "lastname": "Martinez"},
    {"name": "Coc", "lastname": "Lopez", "age": 35}
]

def get_user_age(userindex=int(input("Ingrese el índice del usuario: "))):
    try:
        print("La edad del usuario " + users[userindex]["name"] + " es: " + str(users[userindex]["age"]))
    except KeyError:
        print("No se encontró la clave 'age' en el usuario " + users[userindex]["name"])


get_user_age()