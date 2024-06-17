# importación de módulos
from producto import Producto
from tienda import Restaurante, Supermercado, Farmacia

# Función para crear una tienda.
Parar = False
def c_store():
    global Parar
    while True:
        type_store = int(input("Ingrese tipo de tienda:\n"" (1) Restaurante\n"" (2) Supermercado\n"" (3) Farmacia\n"))
        if type_store > 3:
            Parar = True
            break
        name_store = input("Ingrese el nombre de la tienda: \n")  
        costo_delivery = float(input("Ingrese el costo de delivery: \n"))
        if type_store == 1:
            return Restaurante(name_store, costo_delivery)
        elif type_store == 2:
            return Supermercado(name_store, costo_delivery)
        elif type_store == 3:
            return Farmacia(name_store, costo_delivery)

# Función para ingresar productos a una tienda.
salir = False
def ingresar_productos(tienda):
    global salir
    while True:
        opcion = int(input("Elija:\n"" (1) Ingresar producto\n"" (2) Salir\n"))
        if opcion == 2:
            salir = True
            break
        name_product = input("Ingrese el nombre del producto: \n")
        price_product = float(input("Ingrese el precio del producto: \n"))
        stock_product = int(input("Ingrese el stock del producto: \n"))
        producto = Producto(name_product, price_product, stock_product)
        tienda.ingresar_producto(producto, stock_product)

# Función principal del programa.       
def main():
    global salir
    global Parar
    tienda = c_store()
    if Parar:
        return
    ingresar_productos(tienda)
    while not salir:
        opcion = int(input("Elija una opción:\n"" (1) Listar productos existentes\n"" (2) Realizar una venta\n"" (3) Salir \n"))
        if opcion == 1:
            print(tienda.listar_productos())
        elif opcion == 2:
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.realizar_venta(nombre_producto, cantidad)
        elif opcion == 3:
            break

if __name__ == "__main__":
    main()