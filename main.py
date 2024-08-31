from Producto_modelo import Producto_modelo
from Categoria import Categoria
from Proveedor import Proveedor
from Bodega import Bodega


def registrar_categoria(categorias):
    nombre = input("Ingrese el nombre de la categoría: ")
    descripcion = input("Ingrese la descripción de la categoría: ")
    categoria = Categoria(nombre, descripcion)
    categorias[nombre] = categoria
    print("Categoría registrada con éxito.\n")

def registrar_producto(productos, categorias):
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock inicial del producto: "))
    categoria_nombre = input("Ingrese el nombre de la categoría del producto: ")
    
    if categoria_nombre in categorias:
        categoria = categorias[categoria_nombre]
        producto = Producto_modelo(nombre, descripcion, precio, stock, categoria)
        productos[nombre] = producto
        categoria.agregar_producto(producto)
        print("Producto registrado con éxito.\n")
    else:
        print("Categoría no encontrada.\n")

def registrar_proveedor(proveedores):
    nombre = input("Ingrese el nombre del proveedor: ")
    direccion = input("Ingrese la dirección del proveedor: ")
    telefono = input("Ingrese el teléfono del proveedor: ")
    proveedor = Proveedor(nombre, direccion, telefono)
    proveedores[nombre] = proveedor
    print("Proveedor registrado con éxito.\n")

def registrar_bodega(bodegas):
    nombre = input("Ingrese el nombre de la bodega: ")
    ubicacion = input("Ingrese la ubicación de la bodega: ")
    capacidad_maxima = int(input("Ingrese la capacidad máxima de la bodega: "))
    bodega = Bodega(nombre, ubicacion, capacidad_maxima)
    bodegas[nombre] = bodega
    print("Bodega registrada con éxito.\n")

def gestionar_stock(productos, operacion):
    nombre_producto = input("Ingrese el nombre del producto: ")
    
    if nombre_producto in productos:
        producto = productos[nombre_producto]
        cantidad = int(input(f"Ingrese la cantidad a {operacion}: "))
        
        if operacion == "agregar":
            producto.agregar_stock(cantidad)
        elif operacion == "retirar":
            producto.retirar_stock(cantidad)
        print(f"Stock {operacion}ado con éxito.\n")
    else:
        print("Producto no encontrado.\n")

def consultar_informacion(productos, categorias, proveedores, bodegas):
    print("Seleccione una opción:")
    print("1. Consultar información de un producto")
    print("2. Consultar información de una categoría")
    print("3. Consultar información de un proveedor")
    print("4. Consultar información de una bodega")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        nombre_producto = input("Ingrese el nombre del producto: ")
        if nombre_producto in productos:
            producto = productos[nombre_producto]
            print(producto)
        else:
            print("Producto no encontrado.\n")
    elif opcion == "2":
        nombre_categoria = input("Ingrese el nombre de la categoría: ")
        if nombre_categoria in categorias:
            categoria = categorias[nombre_categoria]
            print(categoria)
        else:
            print("Categoría no encontrada.\n")
    elif opcion == "3":
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        if nombre_proveedor in proveedores:
            proveedor = proveedores[nombre_proveedor]
            print(proveedor)
        else:
            print("Proveedor no encontrado.\n")
    elif opcion == "4":
        nombre_bodega = input("Ingrese el nombre de la bodega: ")
        if nombre_bodega in bodegas:
            bodega = bodegas[nombre_bodega]
            print(bodega)
        else:
            print("Bodega no encontrada.\n")
    else:
        print("Opción no válida.\n")

def menu_principal():
    productos = {}
    categorias = {}
    proveedores = {}
    bodegas = {}

    while True:
        print("Sistema de Gestión de Inventario")
        print("1. Registrar categoría")
        print("2. Registrar producto")
        print("3. Registrar proveedor")
        print("4. Registrar bodega")
        print("5. Agregar stock a un producto")
        print("6. Retirar stock de un producto")
        print("7. Consultar información")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_categoria(categorias)
        elif opcion == "2":
            registrar_producto(productos, categorias)
        elif opcion == "3":
            registrar_proveedor(proveedores)
        elif opcion == "4":
            registrar_bodega(bodegas)
        elif opcion == "5":
            gestionar_stock(productos, "agregar")
        elif opcion == "6":
            gestionar_stock(productos, "retirar")
        elif opcion == "7":
            consultar_informacion(productos, categorias, proveedores, bodegas)
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu_principal()
