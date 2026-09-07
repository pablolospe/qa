import pytest
# [CÓDIGO PROPIO]: Importamos nuestro archivo/módulo a testear (productos.py)
import productos

#decoradores
@pytest.fixture(autouse=True)
def limpiar_productos():
    productos.productos.clear()
    yield # => se ejecutan los test (continua ejecucion)
    productos.productos.clear()

@pytest.fixture()
def datos_base():
    productos.productos.extend([
        {"nombre": "pan", "precio": 10, "cantidad": 1},
        {"nombre": "leche", "precio": 10, "cantidad": 1},
        {"nombre": "gaseosa", "precio": 10, "cantidad": 1},
    ])
    return productos.productos


# [CONVENCIÓN DE PYTEST]: Los tests deben empezar con "test_" para que pytest los detecte automáticamente.
# [PYTEST FIXTURE]: 'monkeypatch' NO se importa; Pytest lo inyecta automáticamente por su nombre.
def test_agregar_producto(monkeypatch):

    # [CÓDIGO PROPIO + PYTHON PURO]: Accedemos a la lista del módulo y usamos .clear() (método nativo de listas en Python)
    productos.productos.clear()

    # [PYTHON PURO / BUILT-INS]:
    # - iter(): Función nativa de Python (built-in) que convierte una lista en un iterador para sacar elementos uno a uno.
    entrada = iter(["pepe", "1", "1"])  # Simula lo que el usuario escribiría en cada input() (nombre, precio, cantidad)

    # [PYTEST - MONKEYPATCH]:
    # - .setattr(): Método de la fixture monkeypatch para reemplazar atributos o funciones temporalmente.
    # - 'builtins.input': 'builtins' es el módulo nativo interno de Python donde vive la función input().
    # - lambda _: Función anónima nativa de Python. Recibe el mensaje que muestra input (ej: "Ingrese el nombre: ") y lo descarta (_).
    # - next(): Función nativa (built-in) que pide el siguiente elemento del iterador 'entrada'.
    monkeypatch.setattr('builtins.input', lambda _: next(entrada))

    # [CÓDIGO PROPIO]: Ejecutamos la función real a probar (internamente llamará a los input() simulados)
    productos.agregar_producto()

    # [PYTHON PURO + PYTEST]:
    # - 'assert': Palabra clave nativa de Python para validar que una condición sea True.
    # - Pytest intercepta 'assert' para mostrar reportes detallados y legibles si falla.
    # - len(): Función nativa de Python (built-in).
    assert len(productos.productos) == 1
    assert productos.productos[0]["nombre"] == "pepe"
    assert len(productos.productos) == 1

def test_datos_duplicados():
    productos.productos.clear()


def test_chekear_productos( datos_base ):
    assert len(datos_base) == 3
