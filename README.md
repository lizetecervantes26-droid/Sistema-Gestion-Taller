# Sistema de Gestión de Servicios para Taller Mecánico

## Descripción

Este proyecto fue desarrollado como parte de la Unidad III de la materia de Programación Orientada a Objetos.

La aplicación permite administrar los servicios realizados en un taller mecánico mediante una interfaz gráfica desarrollada con Tkinter y una base de datos MySQL. El sistema facilita el registro, consulta, actualización y eliminación de servicios, además de incorporar validaciones, manejo de excepciones y pruebas unitarias para mejorar su funcionamiento.

---

## Funcionalidades

- Registro de servicios.
- Consulta de todos los servicios registrados.
- Búsqueda dinámica por cliente, vehículo o tipo de servicio.
- Actualización de información.
- Eliminación de registros.
- Validación de datos.
- Manejo de excepciones personalizadas.
- Pruebas unitarias con Pytest.

---

## Tecnologías utilizadas

- Python 3
- Tkinter
- MySQL
- Pytest
- Programación Orientada a Objetos (POO)

---

## Estructura del proyecto

```
CRUD/
│
├── conexion.py
├── servicio.py
├── repositorio_serv.py
├── controlador_serv.py
├── interfaz_v2.py
├── main.py
├── db_taller.sql
│
├── exceptions/
│   ├── costo_invalido.py
│   └── servicio_no_encontrado.py
│
└── tests/
    ├── test_controlador.py
    └── test_repositorio.py
```

---

## Requisitos

Antes de ejecutar el proyecto es necesario tener instalado:

- Python 3
- MySQL
- Las librerías necesarias del proyecto

---

## Ejecución

1. Clonar el repositorio.

2. Crear la base de datos utilizando el archivo:

```
db_taller.sql
```

3. Configurar los datos de conexión en:

```
conexion.py
```

4. Ejecutar el archivo principal:

```bash
python main.py

## Pruebas unitarias

El proyecto incluye pruebas unitarias desarrolladas con Pytest para validar las principales reglas de negocio y las operaciones del repositorio.

Para ejecutar las pruebas:

```bash
pytest -v

## Autor

**Lizete Cervantes**

Universidad Tecnológica de Querétaro (UTEQ)

Tecnologías de la Información e Innovación Digital

Proyecto Unidad III - Programación Orientada a Objetos