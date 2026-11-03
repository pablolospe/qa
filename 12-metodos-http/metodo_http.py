import requests

def obtener_publicaciones(post_url):
    respuesta = requests.get(f"{post_url}")
    return respuesta


def obtener_una_publicacion(post_url):
    respuesta = requests.get(f"{post_url}/1")
    return respuesta


def crear_publicacion(post_url):
    datos = {
        "title": "Publicacion de prueba",
        "body": "Contenido de la publicacion",
        "userId": 1
    }
    respuesta = requests.post(f"{post_url}", json=datos)
    return respuesta

def modificar_publicacion(post_url):
    datos = {
        "title": "Publicacion modificada",
        "body": "Contenido modificado",
        "userId": 1
    }
    respuesta = requests.put(f"{post_url}/1", data=datos)
    return respuesta

def eliminar_publicacion(post_url):
    respuesta = requests.delete(f"{post_url}/1")
    return respuesta