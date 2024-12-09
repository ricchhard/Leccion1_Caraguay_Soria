# Leccion1_Caraguay_Soria

Este proyecto es un sistema de gestión de ventas que incluye funcionalidades para manejar las entidades de **Productos** y **Categorías**. Además, se ha desarrollado una capa SOAP para exponer operaciones CRUD de ambas entidades, permitiendo la integración con aplicaciones externas.

---

## **Estructura del Proyecto**

El proyecto está organizado en las siguientes capas:

1. **BLL (Business Logic Layer):**
   - Contiene la lógica de negocio para las entidades **Productos** y **Categorías**.
   - Maneja operaciones CRUD y valida reglas de negocio.

2. **DAL (Data Access Layer):**
   - Gestiona las interacciones con la base de datos.
   - Implementa patrones como repositorio para desacoplar la lógica de negocio de la persistencia de datos.

3. **Entities:**
   - Define las clases que representan las tablas de la base de datos (**Productos** y **Categorías**).

4. **Service:**
   - Implementa servicios web SOAP que exponen operaciones CRUD para integración con aplicaciones externas.

5. **NWind.MVCPLS:**
   - Aplicación web basada en ASP.NET MVC que actúa como interfaz de usuario.
   - Permite gestionar los datos a través de formularios y tablas dinámicas.

---

## **Funcionalidades Principales**

### **Gestión de Productos**
- Crear, leer, actualizar y eliminar productos.
- Validación de las unidades en existencia antes de permitir la eliminación.

### **Gestión de Categorías**
- Crear, leer, actualizar y eliminar categorías.
- Validación para evitar duplicados al crear nuevas categorías.

### **Capa SOAP**
- **URL del Servicio SOAP:**  
https://localhost:44362/CategoriesService.asmx

https://localhost:44362/ProductsService.asmx
- Métodos disponibles para categorías:
- `GetCategories`: Devuelve una lista de categorías.
- `AddCategory`: Agrega una nueva categoría.
- `UpdateCategory`: Actualiza una categoría existente.
- `DeleteCategory`: Elimina una categoría si no tiene dependencias.

---

## **Requisitos del Proyecto**

- **Entorno de Desarrollo:**
- Visual Studio 2022 o superior.
- .NET Framework 4.8.

- **Dependencias:**
- Entity Framework (para la capa DAL).
- ASP.NET MVC (para la aplicación web).
- Herramientas para SOAP (SoapUI para pruebas).

---

## **Realizado por:**
Caraguay Richard

Soria Mikela
