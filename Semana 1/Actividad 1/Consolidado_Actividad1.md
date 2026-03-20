# Actividad 1

Reporte: Solución de Ciencia de Datos para DeportivaMX

Perfiles de ciencia de datos

- **Ingeniero de datos**
  - Se encarga de construir y mantener la infraestructura de datos.
  - Es clave para manejar grandes volúmenes de información y asegurar que los datos estén disponibles.

- **Data Scientist**
  - Analiza los datos y genera modelos para identificar patrones.
  - Ayuda a entender el comportamiento de clientes y mejorar decisiones.

- **Analista de datos**
  - Interpreta datos y crea reportes.
  - Facilita la toma de decisiones.

- **Ingeniero de Machine Learning**
  - Implementa modelos predictivos (recomendaciones, ventas, etc.).
  - Mejora la experiencia del cliente con personalización.

---

🔹 **Las 5 V del Big Data**

- **Volumen**
  - DeportivaMX genera grandes cantidades de datos (ventas, clientes, productos, etc).

- **Velocidad**
  - Los datos se generan en tiempo real.

- **Variedad**
  - Hay datos estructurados (ventas) y no estructurados (reseñas, comportamiento web).

- **Veracidad**
  - Es necesario limpiar y validar los datos para evitar errores.

- **Valor**
  - Los datos permiten mejorar la experiencia del cliente y aumentar ventas.

---

Arquitectura de almacenamiento (simplificada)

**Propuesta:**
- Apache Hadoop + MongoDB

---

**Componentes**

- **Apache Hadoop**
  - Almacena grandes volúmenes de datos en bruto (ventas, logs, comportamiento web).
  - Permite escalabilidad y almacenamiento distribuido.

- **MongoDB**
  - Base de datos NoSQL documental.
  - Guarda datos estructurados y semiestructurados como:
    - Clientes
    - Productos
    - Ventas
  - Flexible gracias a su formato JSON.

---

**Flujo de datos**

1. Los datos se recolectan desde la tienda (ventas, usuarios, etc.).
2. Se almacenan en Hadoop como datos en bruto.
3. Los datos importantes y limpios se guardan en MongoDB.
4. Desde MongoDB se pueden consultar para análisis y visualización.

---

**Justificación**

- Hadoop permite manejar grandes volúmenes de datos sin límites.
- MongoDB facilita el acceso rápido y flexible a la información.
- La combinación es escalable, eficiente y fácil de implementar.
- Reduce complejidad al usar solo dos tecnologías clave.

Colecciones JSON

- **[Coleccion Cliente](Coleccion/Cliente.json)**
- **[Coleccion Productos](Coleccion/Productos.json)**
- **[Coleccion Reseñas](Coleccion/Reseñas.json)**
- **[Coleccion Ventas](Coleccion/Ventas.json)**