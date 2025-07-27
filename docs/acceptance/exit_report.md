# Informe de Salida

## Resumen Ejecutivo

Este proyecto tuvo como objetivo desarrollar e implementar un modelo de machine learning para la detección de fraude transaccional de tarjetas de crédito. Se utilizó un modelo de Regresión Logística, el cual fue desplegado exitosamente como una API en la plataforma Render. El modelo mostró un buen desempeño con un recall del 89.85%, siendo una solución efectiva y eficiente para la detección de fraudes.

## Resultados del proyecto

- **Entregables:**
  - Modelo de detección de fraude entrenado y validado.
  - API REST desplegada en Render (`https://mlds6-fraud-detection-api.onrender.com`).
  - Documentación completa del modelo y del despliegue.
    
- **Evaluación del modelo:**
  - **Recall:** 89.85%
  - **Precisión:** 82.96%
  - **ROC AUC:** 97.49%
- **Relevancia:** El modelo permite identificar la gran mayoría de transacciones fraudulentas, lo cual es crucial para minimizar pérdidas por fraude.

## Lecciones aprendidas

- **Desafíos:** La principal dificultad fue resolver las incompatibilidades de versiones entre el entorno de entrenamiento local y el entorno de producción en Render, lo que requirió una gestión cuidadosa de las dependencias (`scikit-learn`, `numpy`, 'pandas'). También se enfrentó el desafío de configurar correctamente el entorno de ejecución de Python en Render, incluyendo la necesidad de definir explícitamente la variable de entorno `PYTHON_VERSION=3.11.11` y asegurar que las rutas de los archivos del modelo fueran correctas. Además, se manejaron advertencias de seguridad relacionadas con la carga de modelos (`InconsistentVersionWarning`) debido a diferencias en las versiones de las bibliotecas usadas para entrenar y cargar el modelo.
- **Aprendizajes:** La importancia de mantener un entorno consistente entre desarrollo y producción. El despliegue en la nube requiere atención a detalles como variables de entorno, estructura de archivos y compatibilidad de versiones de librerías.
- **Recomendaciones:** Para futuros proyectos, se recomienda el uso de entornos virtuales con versiones fijas (`pip freeze`) y considerar formatos de serialización más robustos como `ONNX` o `skops.io` para mejorar la portabilidad, seguridad y mantenibilidad del modelo.
- Es crucial documentar y mantener sincronizadas las versiones de todas las dependencias entre los entornos de entrenamiento y despliegue.

## Impacto del proyecto

- **Impacto:** El modelo proporciona una herramienta automatizada para detectar fraudes, lo que puede reducir significativamente las pérdidas financieras asociadas.
- **Áreas de mejora:** Implementar autenticación en la API, monitoreo de predicciones, logging robusto, y un proceso de reentrenamiento automático del modelo con nuevos datos. Migrar a un servidor WSGI para producción en lugar del servidor de desarrollo de Flask. Mejorar la gestión del ciclo de vida del modelo y las dependencias.

## Conclusiones

- Se logró desarrollar y desplegar con éxito un modelo de detección de fraudes con métricas sólidas.
- El despliegue en Render demostró ser una solución accesible y efectiva para poner el modelo en producción, aunque requiere una configuración inicial cuidadosa para resolver problemas de entorno y dependencias.
- Se recomienda mantener el modelo actualizado, extender la API con funcionalidades de monitoreo y seguridad, y considerar estrategias más robustas para la persistencia del modelo para un uso en producción a largo plazo.

## Agradecimientos

- Agradecezco a la Universidad Nacional de Colombia y sus colaboradores por el curso impartido.
