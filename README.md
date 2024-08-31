# EJERCICIO 2 - PROGRAMACION I
## SISTEMA DE GESTIÓN DE INVENTARIOS

![Diagrama de Clases](https://iccsi.com.ar/wp-content/uploads/como-funciona-la-gestion-inteligente-de-inventario.webp)

## Descripción

Un **Sistema de Gestión de Inventario** facilita la gestión de productos, categorías, proveedores y bodegas. Este sistema permite:

- **Registrar** nuevas categorías, productos, proveedores y bodegas.
- **Gestionar** el stock de productos, con opciones para agregar y retirar unidades.
- **Consultar** información sobre productos, categorías, proveedores y bodegas existentes.


## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes herramientas:

- **Python**: 3.x (Se recomienda la última versión estable)

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

- `producto_modelo.py`: Define la clase `ProductoModelo`, que representa los productos en el inventario.
- `categoria.py`: Define la clase `Categoria`, que representa las categorías de productos.
- `proveedor.py`: Define la clase `Proveedor`, que representa los proveedores.
- `bodega.py`: Define la clase `Bodega`, que representa las bodegas.
- `main.py`: Contiene la lógica principal del sistema y maneja la interacción con el usuario.

### Diagrama de Clases UML

El diagrama de clases UML para el sistema es el siguiente:

![Diagrama de Clases](https://res.cloudinary.com/dsn4ukokp/image/upload/v1724473149/DIAGRAMA_UML_tvs4pn.png)

# Instalación y Ejecución

Clona el Repositorio:
Si estás utilizando Git, clona el repositorio a tu máquina local:

```bash
git clone <URL_DEL_REPOSITORIO>
```
Alternativamente, descarga el archivo ZIP del repositorio y descomprímelo.

# Ejecución

1. Navega al Directorio del Proyecto:

	Abre una terminal o consola de comandos y navega al directorio donde se encuentran los archivos del proyecto:
```bash
cd ruta/del/directorio
```
Ejecuta el Archivo Principal:

2. Ejecuta el ejercicio con el siguiente comando
```bash
python main.py
```

3. Uso de la Aplicación:

	Una vez que la aplicación esté en ejecución, sigue las instrucciones en la consola para:
Registrar categorías (1 en el menú).
Registrar productos (2 en el menú).
Registrar proveedores (3 en el menú).
Registrar bodegas (4 en el menú).
Agregar stock a productos (5 en el menú).
Retirar stock de productos (6 en el menú).
Consultar información sobre productos, categorías, proveedores y bodegas (7 en el menú).
Salir de la aplicación (8 en el menú).

# Funcionalidades

- **Registrar Categoría:** Permite añadir nuevas categorías con un nombre y descripción.
- **Registrar Producto:** Permite añadir productos con nombre, descripción, precio, stock inicial y categoría asociada.
- **Registrar Proveedor:** Permite añadir proveedores con nombre, dirección y teléfono.
- **Registrar Bodega:** Permite añadir bodegas con nombre, ubicación y capacidad máxima.
- **Gestionar Stock:** Permite agregar o retirar unidades de stock para productos existentes.
- **Consultar Información:** Permite visualizar la información detallada sobre productos, categorías, proveedores y bodegas.

# Validaciones del ejercicio

- **Categorías Existentes:** Verifica si una categoría existe antes de registrar un producto.
- **Stock Suficiente:** Verifica que haya suficiente stock antes de permitir la retirada de unidades.

# AUTOR
**Daniel Steven Chavez Valdes**
**Ingeniería de Sistemas 4 Semestre**
**Universidad Libre Seccional Cali**
