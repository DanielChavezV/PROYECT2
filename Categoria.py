class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        producto.categoria = self
    
    def eliminar_producto(self, producto):
        self.productos.remove(producto)
        producto.categoria = None