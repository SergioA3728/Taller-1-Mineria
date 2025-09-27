# Dataset Sintético de Deserción Estudiantil

Este dataset fue generado en Python para simular información de estudiantes universitarios y predecir la **deserción (abandono) en el primer año académico**.  
Contiene datos demográficos, académicos y financieros con **500 registros**.

---

## Archivo
`Dataset_desercion_estudiantil.csv`

- **Filas (estudiantes):** 500  
- **Columnas (variables):** 10

---

## Variables

| Columna                  | Tipo        | Rango / Categorías                   | Descripción |
|--------------------------|------------|---------------------------------------|------------|
| **Edad**                | Entero     | 16–29 años (con algunos outliers de 45) | Edad del estudiante. |
| **Genero**              | Categórica | 'M' o 'F'                             | Género del estudiante. |
| **Lugar Origen**        | Categórica | 'Soledad', 'Sabana Larga', 'Sabana Grande', 'Baranoa', 'Barranquilla' | Ciudad/municipio de origen. |
| **Promedio del Bachiderato** | Decimal   | 2.0–5.0 (outliers de 10)             | Promedio de calificaciones en bachillerato. |
| **ICFES**               | Decimal    | 200–500                               | Puntaje de la prueba ICFES (examen de admisión en Colombia). |
| **Notas Semestre #1**   | Decimal    | 2.0–5.0                                | Promedio de calificaciones en el primer semestre universitario. |
| **Estrato**             | Entero     | 1–6                                    | Nivel socioeconómico colombiano. |
| **Beca**                | Categórica | 'Si' o 'No'                            | Indica si el estudiante tiene beca. |
| **Credito Academico**   | Categórica | 'Si' o 'No'                            | Indica si el estudiante posee crédito del Icetex u otra entidad. |
| **Desercion**           | Categórica | 'Si' o 'No'                            | Variable objetivo: indica si el estudiante desertó. |

---

## Generación de Datos

- **Cantidad:** 500 registros.  
- **Aleatoriedad:** Se utilizó `numpy` y `random` con semilla 42 para reproducibilidad.  
- **Dependencia de la variable objetivo:**  
  - Mayor probabilidad de deserción cuando el promedio de bachillerato o las notas del primer semestre son menores a 3.0.

---

## Valores Especiales

### Valores Nulos
Se introdujo aproximadamente un **5 % de valores faltantes** en:
- `Promedio del Bachiderato`
- `Notas Semestre #1`
- `Estrato`

### Outliers
- **Edad:** 5 registros con valor **45** (fuera del rango esperado de 16–29).  
- **Promedio del Bachiderato:** 5 registros con valor **10** (fuera del rango 2.0–5.0).

---

## Código de Generación
El dataset fue creado con Python usando las librerías:
- `pandas`
- `numpy`
- `random`

El script completo se encuentra en este repositorio.

---

## Uso
Este dataset es únicamente "simulado" y sirve para:
- Pruebas de algoritmos de Machine Learning (clasificación binaria).
- Ejercicios de limpieza de datos: manejo de nulos y outliers.
- Ejemplos educativos en minería de datos y predicción de deserción estudiantil.
