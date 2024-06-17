# Clase base que representa una tienda.
class Tienda:

    # Constructor de la clase Tienda.
    def __init__(self, nombre: str, costo_delivery: int) -> None:
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = {}
    
    # Método para ingresar un producto a la tienda.
    def ingresar_producto(self, producto, cantidad):
        if producto.nombre in self.__productos:
            self.__productos[producto.nombre].stock += cantidad
        else:
            self.__productos[producto.nombre] = producto

    # Método para listar los productos de la tienda.
    def listar_productos(self):
        return "\n".join([f"{p.nombre}: {p.precio}" for p in self.__productos.values()])
    
    # Método para realizar una venta.
    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad <= 0:
            return 0
        if nombre_producto in self._productos:
            if self.__productos[nombre_producto].stock >= cantidad:
                self.__productos[nombre_producto].stock -= cantidad
                return cantidad
            else:
                cantidad_vendida = self.__productos[nombre_producto].stock
                self.__productos[nombre_producto].stock = 0
                return cantidad_vendida
        else:
            pass
        return 0


# Clase que representa una tienda de tipo Restaurante.        
class Restaurante(Tienda):

    # Método para ingresar un producto a la tienda.
    def ingresar_producto(self, producto, cantidad):
        producto.stock = 0
        super().ingresar_producto(producto, cantidad)


# Clase que representa una tienda de tipo Supermercado.
class Supermercado(Tienda):

    # Método para listar los productos de la tienda.
    def listar_productos(self):
        return "\n".join([f"{p.nombre}: {p.precio}, Stock: {p.stock} {'Pocos productos disponibles' if p.stock < 10 else ''}" for p in self.__productos.values()])


# Clase que representa una tienda de tipo Farmacia.
class Farmacia(Tienda):

    # Método para listar los productos de la tienda.
    def listar_productos(self):
        return "\n".join([f"{p.nombre}: {p.precio} {'Envío gratis al solicitar este producto' if p.precio > 15000 else ''}" for p in self.__productos.values()])
    
    # Método para realizar una venta.
    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            print("No se puede solicitar una cantidad superior a 3 por producto en cada venta en una Farmacia.")
            return 0
        return super().realizar_venta(nombre_producto, cantidad)    