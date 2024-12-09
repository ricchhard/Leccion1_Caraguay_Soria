from zeep import Client
from zeep.transports import Transport
from requests import Session

# Crear una sesión y deshabilitar la verificación SSL
session = Session()
session.verify = False

# Crear un transporte con la sesión modificada
transport = Transport(session=session)

# URL del servicio SOAP (modifica la URL al dominio correspondiente)
wsdl_url = 'https://localhost:44362/CategoriesService.asmx?WSDL'

# Crear el cliente SOAP
client = Client(wsdl_url, transport=transport)

# Obtener todas las categorías
def obtener_categorias():
    try:
        categorias = client.service.GetCategories()
        print("Categorías obtenidas:")
        for categoria in categorias:
            print(f"ID: {categoria.CategoryID}, Nombre: {categoria.CategoryName}, Descripción: {categoria.Description}")
    except Exception as e:
        print(f"Error al obtener categorías: {e}")

# Agregar una nueva categoría
def agregar_categoria(category_name, description):
    try:
        resultado = client.service.AddCategory(category_name, description)
        print(resultado)
    except Exception as e:
        print(f"Error al agregar categoría: {e}")

# Actualizar una categoría existente
def actualizar_categoria(category_id, category_name, description):
    try:
        resultado = client.service.UpdateCategory(category_id, category_name, description)
        print(resultado)
    except Exception as e:
        print(f"Error al actualizar categoría: {e}")

# Eliminar una categoría por su ID
def eliminar_categoria(category_id):
    try:
        resultado = client.service.DeleteCategory(category_id)
        print(resultado)
    except Exception as e:
        print(f"Error al eliminar categoría: {e}")

# Ejemplos de llamadas a los métodos del servicio
if __name__ == "__main__":
    #print("Obteniendo categorías:")
    obtener_categorias()

    #print("\nAgregando una nueva categoría:")
    #agregar_categoria("Nueva Categoría", "Descripción de la nueva categoría")

    #print("\nActualizando una categoría existente:")
    #actualizar_categoria(1010, "Categoría Actualizada", "Descripción actualizada")

    #print("\nEliminando una categoría:")
    #eliminar_categoria(1010)