# Semana 1: Fundamentos de Ciencia de Datos y Big Data

## Ejercicios Complementarios

## Ejercicio 1
![Imagen](/Semana%201/Img/IMG_20260318_153857.jpg)

---

## Ejercicio 2
![Imagen](../Img/Captura%20de%20pantalla%202026-03-18%20152256.png)

---

## Ejercicio 3

| Cantidad | Notación Científica |
|----------|--------------------|
| 1,000,000 bytes | 10⁶ Megabytes |
| 1,000,000,000 registros | 10⁹ Gigaregistros |
| 1,000,000,000,000 bytes | 10¹² Terabytes |

---

## Ejercicio 4
![Imagen](../Img/Captura%20de%20pantalla%202026-03-18%20154316.png)

![Imagen](../Img/Captura%20de%20pantalla%202026-03-18%20154607.png)

![Imagen](../Img/Captura%20de%20pantalla%202026-03-18%20154736.png)


---

## Ejercicio 5

### Factorial

```pseint
Algoritmo Factorial
    Definir n, i, resultado Como Entero

    n <- 5
    resultado <- 1

    Para i <- 1 Hasta n Hacer
        resultado <- resultado * i
    FinPara

    Escribir "El factorial de ", n, " es: ", resultado
FinAlgoritmo
```

---

### Lista

```pseint
Algoritmo BuscarElemento
    Definir lista, i, n, buscado Como Entero
    Definir encontrado Como Logico

    n <- 5
    Dimension lista[n]

    lista[1] <- 10
    lista[2] <- 20
    lista[3] <- 30
    lista[4] <- 40
    lista[5] <- 50

    buscado <- 30
    encontrado <- Falso

    Para i <- 1 Hasta n Hacer
        Si lista[i] = buscado Entonces
            encontrado <- Verdadero
        FinSi
    FinPara

    Si encontrado Entonces
        Escribir "Elemento encontrado"
    SiNo
        Escribir "Elemento no encontrado"
    FinSi
FinAlgoritmo
```

---

### Ordenar

```pseint
Algoritmo OrdenarLista
    Definir lista, i, j, n, aux Como Entero

    n <- 5
    Dimension lista[n]

    lista[1] <- 5
    lista[2] <- 2
    lista[3] <- 8
    lista[4] <- 1
    lista[5] <- 3

    Para i <- 1 Hasta n-1 Hacer
        Para j <- 1 Hasta n-1 Hacer
            Si lista[j] > lista[j+1] Entonces
                aux <- lista[j]
                lista[j] <- lista[j+1]
                lista[j+1] <- aux
            FinSi
        FinPara
    FinPara

    Escribir "Lista ordenada:"
    Para i <- 1 Hasta n Hacer
        Escribir lista[i]
    FinPara
FinAlgoritmo
```

---

## Ejercicio 6

- False  
- True  
- True  
- True  
- True  

---

## Ejercicio 7

**¿Quién es considerada la primera científica de datos?**  
Ada Lovelace (1815-1852)

**¿Qué es el "Data Science Venn Diagram" de Drew Conway?**  
Es una representación visual que define la ciencia de datos en la intersección de tres áreas clave: habilidades de hacking (programación), conocimiento matemático/estadístico y experiencia en el dominio.

**Menciona 3 herramientas modernas de Big Data**

- MongoDB  
- Apache Spark  
- Databricks  

---

## Ejercicio 8

### Caso Salud
**Diagnóstico y Predicción con IA (IBM Watson/DeepMind):**  
Se utilizan grandes conjuntos de datos de historiales médicos y estudios de imágenes para crear asistentes cognitivos que ayudan a los médicos a identificar patrones, realizar diagnósticos más rápidos y precisos, y predecir la respuesta a tratamientos.

---

### Caso Finanzas
**Detección de Fraudes:**  
Analiza patrones de gasto, geolocalización y dispositivos en tiempo real para bloquear operaciones sospechosas instantáneamente.

---

### Caso Redes Sociales
**Spotify:**  
Analiza canciones omitidas, playlists creadas y hábitos de escucha para crear "Discover Weekly" y “Daily Mixes” personalizados. Además, utilizan datos para predecir tendencias musicales, acertando incluso en los ganadores de premios Grammy.

---

### Caso Deportes
**Análisis del Rival:**  
Equipos como el Manchester City utilizan datos para identificar patrones de juego, áreas de presión y debilidades del contrincante, permitiendo anticipar los movimientos rivales.
