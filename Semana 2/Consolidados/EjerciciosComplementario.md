# Ejercicio 1 SQL
1. 
```sql
SELECT * FROM empleados;

```
2. 
```sql
SELECT nombre, salario
FROM empleados
WHERE departamento = 'IT';
```
3. 
```sql
SELECT *
FROM empleados
ORDER BY salario DESC
LIMIT 1;
```
4.
```sql
SELECT departamento, COUNT(*) AS total_empleados
FROM empleados
GROUP BY departamento;
```

5.
```sql
UPDATE empleados
SET salario = 50000
WHERE nombre = 'María';
```

# Ejercicio 2 SQL

1.
```sql
SELECT empleados.id, empleados.nombre, departamentos.nombre AS departamento
FROM empleados
INNER JOIN departamentos
ON empleados.id_departamento = departamentos.id;
```

2.
```sql
SELECT empleados.id, empleados.nombre, departamentos.nombre AS departamento
FROM empleados
LEFT JOIN departamentos
ON empleados.id_departamento = departamentos.id;
```

3.
```sql
SELECT departamentos.nombre AS departamento, COUNT(empleados.id) AS total_empleados
FROM departamentos
LEFT JOIN empleados
ON empleados.id_departamento = departamentos.id
GROUP BY departamentos.nombre;
```


# Ejercicio 3 y 4 JSON

- **[EjJSON.ipynb](EjJSON.ipynb)**

# Ejercicio 5 y 6 MongoDB

- **[EjMONGO.ipynb](EjMONGO.ipynb)**

# Ejercicio 7

## 1. Bases de datos Documentales
Ejemplos: MongoDB, CouchDB  

### ¿Qué son?
Almacenan datos en documentos tipo JSON (flexibles y sin esquema fijo).

### ¿Cuándo usarlas?
- Aplicaciones web modernas
- APIs
- Sistemas con datos cambiantes

### Ventajas
- Flexibilidad (no necesitas estructura fija)
- Fácil de escalar
- Compatible con JSON

### Desventajas
- Menos eficientes en relaciones complejas
- Puede haber duplicación de datos

---

## 2. Bases de datos Key-Value
Ejemplos: Redis, DynamoDB  

### ¿Qué son?
Guardan datos como pares clave → valor.

### ¿Cuándo usarlas?
- Caché
- Sesiones de usuario
- Aplicaciones en tiempo real

### Ventajas
- Muy rápidas
- Simples
- Alto rendimiento

### Desventajas
- No permiten consultas complejas
- Estructura muy básica

---

## 3. Bases de datos Columnar
Ejemplos: Cassandra, HBase  

### ¿Qué son?
Almacenan datos por columnas en lugar de filas.

### ¿Cuándo usarlas?
- Big Data
- Análisis de grandes volúmenes
- Sistemas distribuidos

### Ventajas
- Escalabilidad horizontal
- Alto rendimiento en consultas masivas

### Desventajas
- Complejas de configurar
- No ideales para transacciones

---

## 4. Bases de datos de Grafos
Ejemplo: Neo4j  

### ¿Qué son?
Trabajan con nodos y relaciones (como redes).

### ¿Cuándo usarlas?
- Redes sociales
- Sistemas de recomendación
- Análisis de relaciones

### Ventajas
- Excelente para relaciones complejas
- Consultas muy rápidas en grafos

### Desventajas
- No son ideales para datos tabulares simples
- Escalabilidad más limitada

---

# Ejercicio 8: Arquitecturas de Almacenamiento

## ¿Qué es un Data Lake?
Un Data Lake es un repositorio que almacena datos en bruto.

### Características:
- Guarda datos estructurados y no estructurados
- No necesita transformación previa
- Muy flexible

### Ejemplo:
Guardar logs, imágenes, videos, JSON sin procesar

---

## ¿Qué es un Data Warehouse?
Un Data Warehouse es un sistema que almacena datos ya procesados y organizados.

### Características:
- Datos limpios y estructurados
- Optimizado para análisis
- Usa esquemas definidos

---

## Diferencias: Data Lake vs Data Warehouse

| Característica | Data Lake | Data Warehouse |
|--------------|----------|---------------|
| Datos | Crudos | Procesados |
| Estructura | Flexible | Fija |
| Uso | Ciencia de datos | BI y reportes |
| Costo | Más barato | Más caro |

---

## OLTP vs OLAP

### OLTP (Online Transaction Processing)
- Operaciones diarias (INSERT, UPDATE)
- Ejemplo: sistema bancario

### OLAP (Online Analytical Processing)
- Análisis de datos
- Consultas complejas

### Diferencias

| OLTP | OLAP |
|------|------|
| Transaccional | Analítico |
| Rápido en operaciones pequeñas | Rápido en consultas grandes |
| Datos actuales | Datos históricos |

---

## ¿Qué es ETL?

ETL = Extract, Transform, Load

### Proceso:
1. Extract (Extraer) → datos de diferentes fuentes  
2. Transform (Transformar) → limpiar y organizar  
3. Load (Cargar) → guardar en Data Warehouse  

### Ejemplo:
- Extraer datos de MongoDB
- Limpiarlos con Python
- Guardarlos en SQL



