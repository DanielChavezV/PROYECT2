class Proveedor:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos_suministrados = []
    
    def agregar_producto(self, producto):
        self.productos_suministrados.append(producto)
    
    def eliminar_producto(self, producto):
        self.productos_suministrados.remove(producto)