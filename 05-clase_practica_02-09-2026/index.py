from productos import (
    agregar_producto,
    mostrar_producto,
    mostrar_productos,
    buscar_producto_por_nombre,
    eliminar_producto,
    buscar_por_precio,
    mostrar_estadisticas,
)
from menu import mostrar_menu



def index():
    while True:
        mostrar_menu()
        op = input("Seleccione una opción: ").strip()

        match op :
            case "1":
                agregar_producto()
            case "2":
                mostrar_producto(int(input("Ingrese el ID del producto a mostrar: ")))
            case "3":
                mostrar_productos()
            case "4":
                buscar_producto_por_nombre(input("Ingrese el nombre del producto a buscar: ").strip())
            case "5":
                eliminar_producto(int(input("Ingrese el ID del producto a eliminar: ")))
            case "6":
                buscar_por_precio()
            case "7":
                mostrar_estadisticas()
            case "8":
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    index()