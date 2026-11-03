import requests
from _pytest.fixtures import fixture
from pytest_check import check # Sirve para ejecutar varios assert y que me muestre todos los que fallan y no solo el primero como suele pasar
import pytest
from metodo_http import (
    obtener_publicaciones,
    obtener_una_publicacion,
    crear_publicacion,
    modificar_publicacion,
    eliminar_publicacion
)

URL_BASE="https://jsonplaceholder.typicode.com"

@pytest.fixture() # que hacia el fixture: ejecutaba codigo antes de cada test que lo utilise
def post_url():
    return f"{URL_BASE}/posts"

@pytest.fixture() # que hacia el fixture: ejecutaba codigo antes de cada test que lo utilise
def user_url():
    return f"{URL_BASE}/users"

def test_get_publicaciones(post_url):
    res = obtener_publicaciones(post_url)

    # verificar que la respuesta sea exitosa 
    assert res.status_code == 200
    # verificar que la respuesta sea un json
    assert res.headers["Content-Type"] == "application/json; charset=utf-8"
    
    # Verificar que la respuesta tenga el formato esperado
    data = res.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # assert all(isinstance(item, dict) for item in data)

    primer_post = data[0]
    assert primer_post["id"] == 1

    # # Verificar los campos
    for post in data:
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post

        assert isinstance(post["userId"], int)
        assert isinstance(post["id"], int)
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)
    
def test_get_una_publicacion(post_url):
    res = obtener_una_publicacion(post_url)
    
    # verificar que la respuesta sea exitosa 
    assert res.status_code == 200
    # verificar que la respuesta sea un json
    assert res.headers["Content-Type"] == "application/json; charset=utf-8"
    
    # Verificar que la respuesta tenga el formato esperado
    data = res.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    

def test_crear_una_publicacion(post_url):
    res = crear_publicacion(post_url)
    
    # verificar que la respuesta sea exitosa 
    assert res.status_code == 201
    # verificar que la respuesta sea un json
    assert res.headers["Content-Type"] == "application/json; charset=utf-8"
    


def test_obtener_usuarios(user_url):
    respuesta = requests.get(user_url)
    datos = respuesta.json()
    print(datos[0])

    check.equal(datos[0]["name"], "Leanne Graham")
    check.equal(respuesta.status_code, 200)
    check.equal(respuesta.headers["Content-Type"], "application/json; charset=utf-8")
    