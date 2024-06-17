# Clase que representa un producto.
class Producto:
    def __init__(self, nombre: str, precio: int, stock: int = 0) -> None:

        # Constructor de la clase Producto.
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)
    
    # Getter del nombre del producto.
    @property 
    def nombre(self):
        return self.__nombre
    
    # Getter del precio del producto.
    @property
    def precio(self):
        return self.__precio

    # Getter del stock del producto.
    @property
    def stock(self):
        return self.__stock
    
    # Setter del stock del producto.
    @stock.setter
    def stock(self, valor):
        self.__stock = max(0, valor)

    # Método para comparar si dos productos son iguales.
    def __eq__(self, product_New):
        return self.__nombre == product_New.__nombre
    
    # Método para sumar el stock de dos productos iguales.
    def __add__(self, product_New):
        if not self.__eq__(product_New):
            return Producto(self.__nombre, self.__precio, self.__stock) 
        return Producto(self.__nombre, self.__precio, self.__stock + product_New.__stock)         
    
    # Método para restar el stock de dos productos iguales.
    def __sub__(self, product_New):
        if not self.__eq__(product_New):
            return Producto(self.__nombre, self.__precio, self.__stock)
        stock_new = self.__stock - product_New.__stock
        if stock_new < 0:
            stock_new = 0
        return Producto(self.__nombre, self.__precio, stock_new)