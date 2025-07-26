# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Detección del fraude transaccional usando técnicas de Machine Learning

## Objetivo del Proyecto

Desarrolar un modelo de Machine Learning con alta capacidad para detectar el fraude transaccional en tarjetas de crédito.

## Alcance del Proyecto

### Incluye:

- Descripción de los datos disponibles:
El proyecto utilizará un conjunto de datos de transacciones con tarjetas de crédito que incluye información sobre el monto, tiempo, y características numéricas anonimizadas de cada transacción, además de una etiqueta indicando si la transacción es fraudulenta o no.

- Descripción de los resultados esperados:
Desarrollar un modelo de machine learning capaz de identificar transacciones fraudulentas con alta precisión, minimizando falsos negativos y proporcionando una herramienta útil para la detección automatizada de fraudes.

- Criterios de éxito del proyecto:
Se busca generar una métricas de desempeño aceptables (>80) para recall y accuracy.

## Metodología

Se utilizará el dataset disponible en Kaggle que contiene transacciones reales etiquetadas, aplicando la metodología CRISP-DM para garantizar un enfoque estructurado en las fases de comprensión del negocio, preparación de datos, modelado y evaluación.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | 
| Preprocesamiento, análisis exploratorio | 2 semanas | 
| Modelamiento y extracción de características | 2 semanas | 
| Despliegue | 1 semana | 
| Evaluación y entrega final | 1 semana | 

## Equipo del Proyecto

- Equipo de ciencia de datos: Cristhian Enrique Córdoba Trillos

## Presupuesto

Desarrollo del modelo: $100 - $200 (tiempo de desarrollo, entrenamiento y optimización)
Implementación en plataforma por definir (Hugging Face/Streamlit/Render/etc.): $25-$50 (alojamiento básico mensual)

## Stakeholders

- Los stakeholders en el proyecto son el equipo de tarjeta de credito del Banco ABC S.A. 
- Los stakeholders actan en la mesa de trabajo como expertos validadores del conocimiento del dominio, dando información clave empírica y de negocio al equipo de ciencia de datos.
- Las expectativas de los stakeholders es la implementación de un modelo de detección del fraude transaccional en tarjetas de crédito que sea funcional y que tenga buena capcacidad de predictibilidad.

## Aprobaciones

- Cristhian Enrique Córdoba Trillos
