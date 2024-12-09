from zeep import Client
from zeep.transports import Transport
from requests import Session

# Crear una sesión y deshabilitar la verificación SSL
session = Session()
session.verify = False

# Crear un transporte con la sesión modificada
transport = Transport(session=session)

# URL del servicio SOAP
wsdl_url = 'https://localhost:44362/ProductsService.asmx?WSDL'

# Crear el cliente SOAP
client = Client(wsdl_url, transport=transport)

# Obtener todos los productos
def obtener_productos():
    try:
        productos = client.service.ObtenerProductos()
        print("Productos obtenidos:")
        for producto in productos:
            print(f"ID: {producto.ProductID}, Nombre: {producto.ProductName}, Categoría ID: {producto.CategoryID}, Precio: {producto.UnitPrice}, Unidades en stock: {producto.UnitsInStock}")
    except Exception as e:
        print(f"Error al obtener productos: {e}")

# Agregar un nuevo producto
def agregar_producto(product_name, category_id, unit_price, units_in_stock):
    try:
        resultado = client.service.AgregarProducto(product_name, category_id, unit_price, units_in_stock)
        print(resultado)
    except Exception as e:
        print(f"Error al agregar producto: {e}")

# Actualizar un producto existente
def actualizar_producto(product_id, product_name, category_id, unit_price, units_in_stock):
    try:
        resultado = client.service.ActualizarProducto(product_id, product_name, category_id, unit_price, units_in_stock)
        print(resultado)
    except Exception as e:
        print(f"Error al actualizar producto: {e}")

# Eliminar un producto por su ID
def eliminar_producto(product_id):
    try:
        resultado = client.service.EliminarProducto(product_id)
        print(resultado)
    except Exception as e:
        print(f"Error al eliminar producto: {e}")

# Llamadas de ejemplo para probar los métodos
#print("Obteniendo productos:")
obtener_productos()

#print("\nAgregando un nuevo producto:")
#agregar_producto("Producto de prueba", 1, 99, 50)

#print("\nActualizando un producto existente:")
#actualizar_producto(1036, "uwu", 2, 70, 0)

#print("\nEliminando un producto:")
#eliminar_producto(1036)
