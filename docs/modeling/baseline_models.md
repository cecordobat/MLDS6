# Reporte del Modelo Baseline - Detección del fraude transaccional en tarjetas de crédito usando un modelo de machine learning

Este documento contiene los resultados del modelo baseline (regresión logística) tomando como punto de referencia un muestreo aleatorio inicial del 10% del total de base de Kaggle (Sparkov Data Generation).

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores.
Las limitaciones de la ejecución en Colab no permite comparar respecto de modelos más complejos como Random Forest, Árboles de decisión, XGB, LightGB, entre otros.

## Variables de entrada

Las variables utilizadas en el modelo son (escaladas):
Variables categóricas:
'category' (del comercio)
'gender'
'state'
'job'
'city'
'merchant'
Variables numéricas:
'amt'
'lat'
'long'
'city_pop'
'merch_lat'
'merch_long'
'day'
'month'
'hour'
'minute'
'age'

## Variable objetivo

* 'Is_Fraud'
* Rango:
    * 1. Transacción fraudulenta
    * 2. Transacción legítima
* Distribución entre clases:
    * 99.4% para legítimas
    * 0.6% para fraudulentas

## Evaluación del modelo

### Distribución después del rebalanceo de clases utilizando SMOTE (generalización de datos)

* Distribución entre clases:
    * 83.4% para legítimas
    * 16.6% para fraudulentas

### Métricas de evaluación

Métricas de desempeño respecto de la base fuera de muestra (OOO).
Accuracy:  0.9523
Precision: 0.8296
Recall:    0.8985
F1-Score:  0.8627
ROC AUC:   0.9749

### Resultados de evaluación

Accuracy (0.9523): Proporción total de predicciones correctas. El modelo acierta en el 95.23% de los casos.

Precision (0.8296): De todos los casos que el modelo predijo como positivos, el 82.96% eran realmente positivos. Mide la calidad de las predicciones positivas.

Recall (0.8985): De todos los casos realmente positivos, el modelo identificó correctamente el 89.85%. Evalúa la capacidad de detectar los positivos reales. Esta es la métrica que buscamos priorizar en el modelo. **

F1-Score (0.8627): Media armónica entre precisión y recall. Equilibra ambas métricas y tiene un valor de 86.27%.

ROC AUC (0.9749): Área bajo la curva ROC. Indica la capacidad del modelo para distinguir entre clases. Un valor de 0.9749 refleja una excelente discriminación.

## Análisis de los resultados
**Fortalezas:**
Excelente capacidad de discriminación (ROC AUC = 97.49%)
* El modelo distingue muy bien entre transacciones fraudulentas y legítimas
* Área bajo la curva casi perfecta, indicando excelente separabilidad
Buen balance entre Precision y Recall (82.96% vs 89.85%)
* Logra capturar el 89.85% de los fraudes reales (Recall)
* De cada 100 alertas, 83 son realmente fraudes (Precision)
Alto accuracy general (95.23%)
* Correctamente clasifica el 95% de todas las transacciones
* Indica buen rendimiento general del modelo
F1-Score sólido (86.27%)
* Buena armonía entre precision y recall
* Modelo equilibrado para el problema de detección de fraude

**Debilidades:**
Precision moderada (82.96%)
* Aproximadamente 17% de las alertas de fraude son falsos positivos
* Puede generar molestias a clientes con transacciones legítimas marcadas como sospechosas
Recall bueno pero no óptimo (89.85%)
* Aproximadamente 10% de los fraudes reales no son detectados
* En un entorno financiero, incluso 10% puede representar pérdidas significativas
Posible overfitting al accuracy
* Con un dataset balanceado (50/50), un accuracy de 95% es excelente
* Pero en producción real (0.5% fraude), el rendimiento puede variar

## Conclusiones

El modelo baseline muestra un buen desempeño general, con una accuracy del 95.23% y una AUC-ROC de 0.9749, lo cual indica una excelente capacidad para distinguir entre clases. Además, el recall (89.85%) sugiere que el modelo identifica correctamente la mayoría de los casos positivos, lo que es especialmente relevante si el problema implica riesgos por falsos negativos (fraude transaccional).

## Referencias
Dataset: [Credit Card Transactions Fraud Detection Dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection/data)

Métricas de desempeño: Accuracy, Precision, Recall, F1-Score, AUC-ROC.
