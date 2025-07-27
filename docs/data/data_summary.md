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

![Variable Objetivo](imagenes/fraude.png)

## Variables individuales

Se analizaron tanto variables categóricas como numéricas:
*   **Variables Categóricas (ej. `category`, `gender`, `state`, `job`):** Se exploró la distribución de categorías y su tasa de fraude asociada. Por ejemplo, la categoría `shopping_net` mostró una alta tasa de fraude, al igual que ciertos trabajos (Air traffic controller, Careers adviser, etc.) y el estado `DE`.
*   **Variables Numéricas (ej. `amt`, `age`, coordenadas geográficas):** Se examinaron sus distribuciones mediante histogramas y boxplots. Se observó que las transacciones fraudulentas tienden a tener montos (`amt`) y edades (`age`) más altos, con una presencia notable de valores atípicos en estas variables.
*   **Transformaciones:** Se crearon nuevas variables a partir de las fechas (`day`, `month`, `year`, `hour`, `minute`) y se calculó la edad (`age`) del titular.

### Distribución de variables numéricas respecto del fraude
![Variable Objetivo](imagenes/boxplot.png)

### Distribución de variables categóricas respecto del fraude
![Variable Objetivo](imagenes/fraud_cats.png)
![Variable Objetivo](imagenes/fraud_geo.png)
![Variable Objetivo](imagenes/fraud_age.png)

## Ranking de variables

Mayores variable con correlación respecto de la variable objetivo:

## Ranking de Variables

Basado en el análisis exploratorio del notebook proporcionado, aquí se presenta un ranking de las variables más influyentes o relevantes para predecir la variable objetivo `is_fraud`, ordenadas de mayor a menor relevancia según la evidencia encontrada:

## Ranking de variables por correlación con `is_fraud`

| Posición | Variable                   | Correlación |
|----------|----------------------------|-------------|
| 1        | city_target_encoded        | 0.27        |
| 2        | amt                        | 0.21        |
| 3        | job_target_encoded         | 0.16        |
| 4        | merchant_target_encoded    | 0.07        |
| 5        | category_target_encoded    | 0.07        |
| 6        | state_target_encoded       | 0.03        |
| 7        | month                      | -0.02       |
| 8        | hour                       | 0.01        |
| 9        | age                        | -0.01       |
| 10       | year                       | 0.01        |
| 11       | gender_target_encoded      | 0.00        |
| 12       | lat                        | 0.00        |
| 13       | long                       | 0.00        |
| 14       | merch_lat                  | 0.00        |
| 15       | merch_long                 | 0.00        |


## Relación entre variables explicativas y variable objetivo

El análisis exploratorio, a partir de la matriz de correlación, reveló varias relaciones interesantes entre las variables explicativas y la variable objetivo `is_fraud`:

*   **Ciudad (`city_target_encoded`):** Es la variable con mayor correlación con el fraude (`0.27`), lo que sugiere que ciertas ciudades tienen una incidencia significativamente más alta de transacciones fraudulentas.
*   **Monto (`amt`):** Presenta una correlación positiva moderada (`0.21`), lo que indica que los fraudes tienden a involucrar montos ligeramente más altos que las transacciones legítimas.
*   **Ocupación (`job_target_encoded`):** Con una correlación de `0.16`, algunas profesiones podrían estar más asociadas a transacciones fraudulentas.
*   **Comerciante (`merchant_target_encoded`):** Con un valor de `0.07`, algunos comerciantes muestran patrones asociados al fraude, aunque la relación es débil.
*   **Categoría (`category_target_encoded`):** También muestra una correlación baja (`0.07`), pero puede estar indicando que ciertas categorías de consumo están más expuestas al fraude.
*   **Estado (`state_target_encoded`):** La correlación es muy baja (`0.03`), lo que sugiere una relación limitada entre el estado geográfico y el fraude.
*   **Variables temporales (`month`, `hour`, `year`):** Muestran correlaciones muy cercanas a cero, por lo que no se observan patrones temporales significativos en este análisis.
*   **Edad (`age`):** Presenta una correlación negativa muy baja (`-0.01`), lo cual indica que no hay una relación lineal clara entre la edad del usuario y la ocurrencia de fraude.
*   **Género (`gender_target_encoded`):** La correlación es nula (`0.00`), lo que sugiere que no se identificó una diferencia relevante entre hombres y mujeres en cuanto a la tasa de fraude.
*   **Coordenadas geográficas (`lat`, `long`, `merch_lat`, `merch_long`):** Todas presentan correlaciones cercanas a cero, lo que confirma que no existe una relación lineal significativa entre la ubicación geográfica y la variable objetivo `is_fraud`.


### MAtriz de Correlaciones
![Variable Objetivo](imagenes/matriz2.png)
