# Ejercicios Actividad 2

# Actividad 2.1: Investigación de Arquitecturas de Datos

## ¿Qué es un Data Warehouse?
Un Data Warehouse es un sistema de almacenamiento de datos diseñado para el análisis y la toma de decisiones.

### Características:
- Almacena datos estructurados
- Datos limpios y procesados
- Orientado a análisis (BI)
- Usa esquemas definidos
- Históricos (no en tiempo real)

---

## ¿Qué es un Data Lake?
Un Data Lake es un repositorio que almacena datos en su forma original (sin procesar).

### Características:
- Almacena datos estructurados y no estructurados
- Alta capacidad de almacenamiento
- Flexible (no requiere esquema previo)
- Ideal para ciencia de datos y Big Data

---



## ¿Qué es un Data Mart?
Un Data Mart es una versión más pequeña de un Data Warehouse, enfocada en un área específica de la organización.

### Características:
- Subconjunto de un Data Warehouse
- Orientado a un departamento (ventas, finanzas, etc.)
- Más rápido y fácil de consultar
- Menor volumen de datos

---

## Comparación: Data Warehouse vs Data Lake

| Característica | Data Warehouse | Data Lake |
|--------------|---------------|----------|
| Tipo de datos | Estructurados | Estructurados y no estructurados |
| Procesamiento | Antes de almacenar | Después de almacenar |
| Estructura | Fija | Flexible |
| Uso | BI y reportes | Análisis avanzado, Big Data |
| Usuarios | Analistas de negocio | Científicos de datos |
| Costo | Más alto | Más bajo |

---


# Actividad 2.2: Introducción a MongoDB

![Imagen](/Semana%202/IMG/Mongo22.png)

# Actividad 2.3 

## **[Act.ipynb](Act2.3/Act.ipynb)**

# Actividad 2.4: Modelado de Datos NoSQL

### Descripción
El sistema permite gestionar libros digitales, usuarios, autores, categorías y préstamos. Los usuarios pueden consultar libros, solicitarlos y devolverlos.

---

## Colecciones

### usuarios
```json
{
  "_id": "ObjectId",
  "nombre": "string",
  "correo": "string",
  "fecha_registro": "date",
  "activo": "boolean"
}
```
### libros
```json
{
  "_id": "ObjectId",
  "titulo": "string",
  "isbn": "string",
  "anio_publicacion": "number",
  "autor_id": "ObjectId",
  "categoria_id": "ObjectId",
  "disponible": "boolean"
}
```
### autores
```json
{
  "_id": "ObjectId",
  "nombre": "string",
  "nacionalidad": "string"
}
```
### categorias
```json
{
  "_id": "ObjectId",
  "nombre": "string",
  "descripcion": "string"
}
```
### prestamos
```json
{
  "_id": "ObjectId",
  "usuario_id": "ObjectId",
  "libro_id": "ObjectId",
  "fecha_prestamo": "date",
  "fecha_devolucion": "date",
  "estado": "string"
}
```
---

## Relaciones

- Usuario → Préstamos (1:N)
- Libro → Préstamos (1:N)
- Libro → Autor (N:1)
- Libro → Categoría (N:1)

---

## Tipos de datos

| Tipo | Descripción |
|------|------------|
| ObjectId | Identificador único |
| string | Texto |
| number | Número |
| boolean | Verdadero o falso |
| date | Fecha |

---

## Justificación

Se usa un modelo con referencias para evitar duplicación de datos.  
Las colecciones separadas mejoran la organización y escalabilidad.  
Permite controlar préstamos, es flexible y facilita consultas comunes.

---

## Ventajas

- Escalable  
- Flexible  
- Evita redundancia  
- Fácil mantenimiento  

---

## Mejoras

- Agregar reseñas de libros  
- Implementar multas por retraso  
- Crear índices en "isbn" y "correo"  