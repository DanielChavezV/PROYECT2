class Producto_modelo:
    def __init__(self, nombre, descripcion, precio, stock, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("No hay suficiente stock para retirar.")

    def __str__(self):
        return f"Producto: {self.nombre}, Descripción: {self.descripcion}, Precio: {self.precio}, Stock: {self.stock}, Categoría: {self.categoria}"
