# Reporte del Modelo Final

## Resumen Ejecutivo

El modelo seleccionado final es un modelo de Regresión Logística con métricas de desmepeño que satisfacen el planteamiento inicial del proyecto para la aceptación del mismo (>85 Recall). 

Adicionalmente, el modelo muestra estas métricas de desempeño:

Accuracy:  0.9523
Precision: 0.8296
Recall:    0.8985
F1-Score:  0.8627
ROC AUC:   0.9749

## Descripción del Problema

El presente proyecto busca resolver el problema de detección de fraude en transacciones financieras, identificando automáticamente operaciones potencialmente fraudulentas a partir de un conjunto de variables relacionadas con el usuario, la ubicación y las características de la transacción.

Este problema se enmarca en el contexto de una entidad financiera que necesita reducir pérdidas económicas y riesgos operativos, mejorando la seguridad de sus sistemas. Para ello, se implementó un modelo de regresión logística, seleccionado por su eficiencia, simplicidad y facilidad de interpretación en problemas de clasificación binaria.

El objetivo principal es predecir la probabilidad de fraude en una transacción y facilitar la toma de decisiones en tiempo real. La elección del modelo también permite justificar sus predicciones ante áreas regulatorias y de auditoría, sirviendo como baseline para futuros modelos más complejos.

## Descripción del Modelo

## Descripción del Modelo

### Modelo Final Seleccionado

El modelo final desarrollado para la detección de fraudes en transacciones de tarjetas de crédito es una **Regresión Logística** con características de regularización L2 y manejo balanceado de clases. Este modelo fue seleccionado por su simplicidad, interpretabilidad y eficiencia computacional, factores cruciales para un sistema de detección de fraudes en tiempo real.

### Arquitectura y Características del Modelo

**Tipo de Modelo**: Regresión Logística Binaria con Regularización L2 (Ridge)
- **Función de activación**: Sigmoide para salida probabilística
- **Regularización**: L2 con parámetro C = 1.0
- **Manejo de clases**: `class_weight='balanced'` para compensar desbalance
- **Solver**: `liblinear` - eficiente para datasets de tamaño medio
- **Máximo de iteraciones**: 1000 iteraciones para convergencia

**Características de Entrada**: 1,856 variables resultantes de:
- **Variables numéricas originales** (11): monto, coordenadas geográficas, población, edad, etc.
- **Variables categóricas codificadas** (1,845): one-hot encoding de categoría, género, estado, ocupación, ciudad y comerciante

### Metodología de Desarrollo

La metodología seguida para el desarrollo del modelo se basó en el enfoque CRISP-DM:

1. **Comprensión del Negocio**: Análisis del problema de detección de fraudes y sus implicaciones financieras
2. **Comprensión de los Datos**: Exploración de variables temporales, demográficas y transaccionales
3. **Preparación de Datos**: 
   - Ingeniería de características temporales (día, mes, hora, etc.)
   - Cálculo de edad a partir de fechas
   - Codificación one-hot de variables categóricas
   - Escalado de variables numéricas mediante StandardScaler
4. **Modelado**: 
   - Balanceo de dataset mediante combinación de SMOTE y undersampling
   - Entrenamiento de Regresión Logística
   - Validación cruzada estratificada (5-fold)
5. **Evaluación**: 
   - Métricas focales: Recall (89.85%) y Precision (82.96%)
   - Análisis de estabilidad mediante validación cruzada
6. **Despliegue**: Exportación de modelo y parámetros para producción

### Técnicas Empleadas

**1. Preprocesamiento Avanzado**:
- **Feature Engineering**: Creación de variables temporales y de edad
- **Codificación**: One-hot encoding para variables categóricas
- **Normalización**: StandardScaler para variables numéricas
- **Manejo de Outliers**: Identificación y tratamiento de valores extremos

**2. Balanceo de Clases**:
- **SMOTE**: Oversampling de la clase minoritaria (fraude) al 10%
- **Undersampling**: Reducción controlada de la clase mayoritaria al 20%
- **Resultado**: Dataset balanceado con 23,456 registros (10% fraude)

**3. Optimización del Modelo**:
- **Regularización L2**: Prevención de overfitting
- **Pesos balanceados**: Compensación automática del desbalance de clases
- **Validación Cruzada**: Evaluación robusta con 5-fold stratified CV

**4. Evaluación Integral**:
- **Métricas múltiples**: Accuracy, Precision, Recall, F1-Score, ROC AUC
- **Análisis de estabilidad**: Coeficiente de variación < 0.1 para todas las métricas
- **Visualizaciones**: Curvas ROC, matrices de confusión, distribución de probabilidades

### Resultados del Modelo Final

- **Accuracy**: 95.23% - Alta precisión general
- **Precision**: 82.96% - Bajo porcentaje de falsos positivos
- **Recall**: 89.85% - Alta detección de fraudes reales. Métrica buscada a optimizar en el desarrollo, mencionado desde la descripción inicial del problema.**
- **F1-Score**: 86.27% - Buen balance entre precision y recall
- **ROC AUC**: 97.49% - Excelente capacidad de discriminación

### Ventajas del Enfoque

1. **Interpretabilidad**: Coeficientes explican la importancia de cada característica
2. **Eficiencia**: Rápido entrenamiento y predicción en tiempo real
3. **Escalabilidad**: Fácil de implementar en producción
4. **Mantenibilidad**: Simple de actualizar y mantener
5. **Transparencia**: Decisiones del modelo pueden ser auditadas y explicadas## Evaluación del Modelo

## Conclusiones y Recomendaciones

### Conclusiones Principales

**1. Efectividad del Modelo**
El modelo de Regresión Logística desarrollado demuestra una **excelente capacidad de detección de fraudes** con un Recall del 89.85%, lo que significa que identifica correctamente el 89.85% de las transacciones fraudulentas reales. Esta métrica es crucial en el contexto de detección de fraudes, donde es preferible tener algunos falsos positivos que dejar pasar fraudes reales.

**2. Balance Óptimo entre Métricas**
El modelo logra un **equilibrio sólido** entre Precision (82.96%) y Recall (89.85%), con un F1-Score de 86.27%. Esto indica que el modelo no solo detecta bien los fraudes, sino que también mantiene un nivel aceptable de precisión en sus alertas.

**3. Alta Discriminación**
Con un ROC AUC de 97.49%, el modelo muestra una **capacidad excepcional de discriminación** entre transacciones legítimas y fraudulentas, lo que lo hace muy confiable para la tarea específica de detección de fraudes.

**4. Estabilidad y Consistencia**
La validación cruzada estratificada demostró que el modelo es **estable y consistente**, con coeficientes de variación menores al 10% para todas las métricas principales, indicando que el rendimiento es robusto y no depende de una división de datos particular.

### Puntos Fuertes del Modelo

**1. Interpretabilidad**
- Coeficientes claramente definidos que explican la influencia de cada variable
- Facilidad para explicar decisiones a stakeholders no técnicos
- Posibilidad de auditoría y cumplimiento regulatorio

**2. Eficiencia Computacional**
- Tiempo de entrenamiento rápido (menos de 1 minuto)
- Predicciones en tiempo real (< 10ms por transacción)
- Bajo consumo de recursos en producción

**3. Escalabilidad**
- Fácil de implementar en diferentes entornos
- Simple de mantener y actualizar
- Compatible con pipelines de machine learning existentes

**4. Robustez**
- Buen manejo del desbalance de clases mediante técnicas de balanceo
- Regularización para prevenir overfitting
- Validación cruzada que confirma estabilidad

### Puntos Débiles y Limitaciones

**1. Falsos Positivos**
- Precision del 82.96% implica que 17% de las alertas son falsas
- En un volumen alto de transacciones, esto puede generar molestias a clientes
- Costo operativo de investigar falsas alertas

**2. Fraudes No Detectados**
- 10.15% de fraudes reales no son identificados
- En el contexto financiero, incluso este porcentaje puede representar pérdidas significativas
- Riesgo de falsa sensación de seguridad

**3. Dependencia de Datos Históricos**
- El modelo solo puede aprender de patrones presentes en los datos de entrenamiento
- Puede no detectar nuevos tipos de fraudes (zero-day attacks)
- Necesidad de reentrenamiento periódico

**4. Limitaciones del Dataset**
- Dataset balanceado artificialmente (10% fraude vs 0.5% real)
- Resultados pueden no reflejar el rendimiento en producción real
- Falta de datos temporales extensos para detectar estacionalidad

### Limitaciones del Proyecto

**1. Ambiente Controlado**
- Pruebas realizadas en condiciones controladas con dataset balanceado
- No se ha validado en el desbalance extremo del mundo real (0.5% fraude)
- Resultados óptimos en laboratorio no garantizan éxito en producción

**2. Características Limitadas**
- No se incluyeron variables de comportamiento del cliente a largo plazo
- Falta de información de dispositivos y navegación web
- Sin datos de redes sociales o perfiles de riesgo extendidos

**3. Sesgos Potenciales**
- Dataset sintético puede no reflejar completamente la realidad
- Posible sobreajuste a patrones específicos del dataset de entrenamiento
- Falta de diversidad geográfica y demográfica real

### Escenarios de Aplicación Recomendados

**1. Implementación Inicial**
- **Sistema de alerta temprana** para transacciones de alto riesgo
- **Capa de filtrado primario** en sistemas de detección de fraudes
- **Herramienta de apoyo** para analistas de fraude

**2. Entornos de Bajo Volumen**
- Instituciones financieras medianas con volumen moderado de transacciones
- Procesadores de pago que buscan solución rápida y efectiva
- Empresas que inician su programa de detección de fraudes

**3. Como Componente de Sistemas Mayores**
- **Primer nivel de screening** en arquitecturas de múltiples capas
- **Modelo base** para ensemble learning con modelos más complejos
- **Sistema de respaldo** cuando modelos complejos fallan

### 🚀 Recomendaciones para Mejora

**1. Mejora Inmediata**
- **Monitoreo continuo** del rendimiento en producción
- **Ajuste de umbrales** basado en costos operativos reales
- **Integración con sistemas** de verificación manual

**2. Desarrollo a Mediano Plazo**
- **Incorporación de features** de comportamiento del cliente
- **Implementación de aprendizaje incremental** para adaptación continua
- **Desarrollo de modelos ensemble** que combinen múltiples enfoques

**3. Estrategia a Largo Plazo**
- **Sistema de feedback** para reentrenamiento con datos reales
- **Integración de inteligencia artificial avanzada** (deep learning, grafos)
- **Desarrollo de perfiles dinámicos** de clientes y comerciantes

**4. Consideraciones de Producción**
- **Implementación gradual** comenzando con transacciones de alto valor
- **Sistema de fallback** para manejo de casos límite
- **Documentación exhaustiva** para mantenimiento y auditoría

### Conclusión Final

El modelo baseline muestra un buen desempeño general, con una accuracy del 95.23% y una AUC-ROC de 0.9749, lo cual indica una excelente capacidad para distinguir entre clases. Además, el recall (89.85%) sugiere que el modelo identifica correctamente la mayoría de los casos positivos, lo que es especialmente relevante si el problema implica riesgos por falsos negativos (fraude transaccional).

## Referencias

Dataset: [Credit Card Transactions Fraud Detection Dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection/data)

Métricas de desempeño: Accuracy, Precision, Recall, F1-Score, AUC-ROC.
