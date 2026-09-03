productos = [{
    "id": 1,
    "nombre": "Producto 1",
    "precio": 10.0,
    "cantidad": 5
    },
    {
    "id": 2,
    "nombre": "Producto 2",
    "precio": 20.0,
    "cantidad": 3
    },
    {
    "id": 3,
    "nombre": "Producto 3",
    "precio": 15.0,
    "cantidad": 7
    }
    ]

def agregar_producto():

    try:
        nombre = input("Ingrese el nombre del producto: \n").strip()

        if not nombre:
            print("Error: El nombre del producto no puede estar vacío.")
            return
        
        precio = float(input("Ingrese el precio del producto: \n").strip())
        cantidad = int(input("Ingrese la cantidad del producto: \n").strip())

        if precio < 0 or cantidad < 0:
            print("Error: El precio y la cantidad deben ser números positivos.")
            return

        producto = {
            "id": len(productos) + 1,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        productos.append(producto)

        print(f"Producto '{nombre}' agregado exitosamente.")

    except ValueError:
        print("Error: El precio debe ser un número válido.")
    finally:
        print("Operacion finalizada.")

def mostrar_producto(id_producto):
    if id_producto is None:
        print("Error: Debe proporcionar un ID de producto.")
        return
    if type(id_producto) != int:
        print("Error: El ID del producto debe ser un número entero.")
        return
    if not productos:
        print("No hay productos para mostrar.")
        return
    if id_producto < 1 or id_producto > len(productos):
        print("Error: ID de producto inválido.")
        return
    for producto in productos:
        if producto["id"] == id_producto:
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
            return

def mostrar_productos():
    if not productos:
        print("No hay productos para mostrar.")
        return
    print(
        """
        ========================
              PRODUCTOS
        ========================
        """)
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
 
def buscar_producto_por_nombre(nombre):
    # que el nombre exista 
    # que el nombre no este vacio
    if nombre is None:
            print("Error: Debe proporcionar un nombre de producto.")
            return
    if not productos:
        print("No hay productos para mostrar.")
        return
    for producto in productos:
        if producto["nombre"].lower() in nombre.lower():
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
            return
 
 
def eliminar_producto(id_producto):
    # el id es numero positivo? existe el producto? 
    if id_producto is None:
        print("Error: Debe proporcionar un ID de producto.")
        return
    if type(id_producto) != int:
        print("Error: El ID del producto debe ser un número entero.")
        return
    if id_producto < 1 or id_producto > len(productos):
        print("Error: ID de producto inválido.")
        return
    producto_a_borrar = next((producto for producto in productos if producto["id"] == id_producto), None)
    if producto_a_borrar is None:
        print("Error: No se encontró un producto con el ID proporcionado.")
        return
    productos.remove(producto_a_borrar)
    print(f"Producto con ID {id_producto} eliminado exitosamente.")
 
def buscar_por_precio():
    print()

def mostrar_estadisticas():
    print()

