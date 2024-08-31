class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos_almacenados = {}
    
    def agregar_producto(self, producto, cantidad):
        if producto.nombre not in self.productos_almacenados:
            self.productos_almacenados[producto.nombre] = 0
        
        total_stock = sum(self.productos_almacenados.values()) + cantidad
        
        if total_stock > self.capacidad_maxima:
            raise ValueError("No hay suficiente espacio en la bodega")
        
        self.productos_almacenados[producto.nombre] += cantidad
        producto.agregar_stock(cantidad)
    
    def retirar_producto(self, producto, cantidad):
        if producto.nombre not in self.productos_almacenados or self.productos_almacenados[producto.nombre] < cantidad:
            raise ValueError("No hay suficiente stock en la bodega")
        
        self.productos_almacenados[producto.nombre] -= cantidad
        producto.retirar_stock(cantidad)
    
    def consultar_disponibilidad(self, producto):
        return self.productos_almacenados.get(producto.nombre, 0)