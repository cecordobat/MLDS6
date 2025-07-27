# Reporte de Datos

## Resumen general de los datos

El conjunto de datos analizado contiene información sobre transacciones de tarjetas de crédito. Se compone de 1,852,394 observaciones (filas) y 22 columnas (variables). No se encontraron valores faltantes ni duplicados en el conjunto de datos. Se realizaron transformaciones iniciales para convertir las columnas de fecha y hora (`trans_date_trans_time`, `dob`) a formato `datetime` y se crearon nuevas variables derivadas como `day`, `month`, `year`, `hour`, `minute`, `year_dob`, y `age`. Luego del procesamiento de datos se crean variables auxiliares y se seleccionan seis (6) variables categóricas para el modelo, así como once (11) variables numéricas para el modelo.

## Resumen de calidad de los datos

La calidad del conjunto de datos es alta en términos de integridad:
*   **Valores Faltantes:** No se encontraron valores nulos en ninguna de las columnas.
*   **Duplicados:** No se identificaron filas duplicadas.
*   **Errores:** No se reportan errores evidentes en los tipos de datos tras las correcciones iniciales.
*   **Valores Extremos:** Se identificaron valores atípicos, especialmente en variables como `amt` (monto de la transacción) y `age` (edad del titular) dentro del subconjunto de transacciones fraudulentas (7,318 y 42 outliers respectivamente, usando el criterio del rango intercuartílico).

## Variable objetivo

La variable objetivo es `is_fraud`, que indica si una transacción es fraudulenta (1) o no (0). La distribución de esta variable muestra un desbalance extremo: la gran mayoría de las transacciones son legítimas (0), mientras que las fraudulentas (1) representan un porcentaje muy pequeño del total. Este desbalance es característico en problemas de detección de fraudes.

![Variable Objetivo](/imagenes/fraude.png)

## Variables individuales

Se analizaron tanto variables categóricas como numéricas:
*   **Variables Categóricas (ej. `category`, `gender`, `state`, `job`):** Se exploró la distribución de categorías y su tasa de fraude asociada. Por ejemplo, la categoría `shopping_net` mostró una alta tasa de fraude, al igual que ciertos trabajos (Air traffic controller, Careers adviser, etc.) y el estado `DE`.
*   **Variables Numéricas (ej. `amt`, `age`, coordenadas geográficas):** Se examinaron sus distribuciones mediante histogramas y boxplots. Se observó que las transacciones fraudulentas tienden a tener montos (`amt`) y edades (`age`) más altos, con una presencia notable de valores atípicos en estas variables.
*   **Transformaciones:** Se crearon nuevas variables a partir de las fechas (`day`, `month`, `year`, `hour`, `minute`) y se calculó la edad (`age`) del titular.

## Ranking de variables

Aunque no se utilizó PCA ni modelos específicos para calcular la importancia en este análisis exploratorio, se puede inferir una relevancia relativa basada en la correlación y el análisis gráfico:
1.  **`amt` (Monto):** Mostró una correlación positiva leve con `is_fraud` y diferencias notables en su distribución entre transacciones fraudulentas y no fraudulentas.
2.  **`category` (Categoría):** Algunas categorías tienen tasas de fraude significativamente más altas.
3.  **`job` (Trabajo):** Algunas profesiones muestran tasas extremas de fraude (100% o 0%).
4.  **`year` (Año):** Alta correlación positiva (0.87) con `is_fraud`.
5.  **Variables de fecha/hora (`month`, `day`, `hour`):** Mostraron patrones en la tasa de fraude.
6.  **`age` (Edad):** Diferencias en la distribución y presencia de outliers en fraudes.
7.  **`state` (Estado) / `city` (Ciudad):** Algunas ubicaciones muestran tasas de fraude más altas.

## Relación entre variables explicativas y variable objetivo

El análisis exploratorio reveló varias relaciones interesantes entre las variables explicativas y la variable objetivo `is_fraud`:
*   **Monto (`amt`):** Las transacciones fraudulentas tienden a tener montos más altos, con una correlación positiva leve (0.22).
*   **Categoría (`category`):** La categoría `shopping_net` tiene una tasa de fraude significativamente más alta.
*   **Género (`gender`):** Se observó una diferencia en la tasa de fraude entre hombres y mujeres.
*   **Ubicación (`state`, `city`, `job`):** Ciertos estados, ciudades y profesiones muestran tasas de fraude extremas.
*   **Fecha y Hora (`month`, `day`, `hour`):** Hay patrones temporales en la ocurrencia de fraudes.
*   **Edad (`age`):** Las transacciones fraudulentas tienden a estar asociadas con edades más altas, siendo el grupo 80-89 el de mayor tasa.
*   **Año (`year`):** Fuerte correlación positiva (0.87) con la variable de fraude.
*   **Coordenadas Geográficas:** No se encontró una relación lineal significativa entre la ubicación del comerciante (`merch_lat`, `merch_long`) y la variable `is_fraud`.
