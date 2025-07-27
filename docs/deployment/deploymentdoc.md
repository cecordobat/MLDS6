# Despliegue de Modelos

## Infraestructura

- **Nombre del modelo:** `modelo_fraude_v1.pkl`
- **Plataforma de despliegue:** [Render](https://render.com/)
  - Render es una plataforma en la nube para desplegar aplicaciones web y APIs de forma gratuita y sencilla. Es compatible con versiones modernas de Python y permite seleccionar la versión deseada. Para especificar la versión de Python, se creó un archivo `.python-version` que indica la versión requerida (en este caso, `3.11.11`). Además, Render utiliza Linux como sistema operativo base.
- **Requisitos técnicos:**
  - Python 3.11.11
  - Bibliotecas: `flask==2.3.3`, `pandas==1.5.3`, `scikit-learn==1.4.2`, `numpy==1.26.4`
  - El servicio se despliega utilizando el entorno de ejecución nativo de Python de Render. Se requiere un archivo `requirements.txt` que contiene las bibliotecas necesarias para el funcionamiento del proyecto. Estas librerías son usadas en mi proyecto para procesar los datos, cargar el modelo y hacer predicciones. El archivo `requirements.txt` asegura que todas las dependencias estén instaladas correctamente en el entorno de producción en Render.
- **Requisitos de seguridad:**
  - El modelo se accede mediante HTTPS.
  - No se requiere autenticación para las predicciones.
  - El modelo se persiste usando `joblib` (basado en `pickle`).

## Código de despliegue

- **Archivo principal:** `app.py`
- **Rutas de acceso a los archivos:**
  - `modelo_fraude_v1.pkl` (modelo entrenado)
  - `scaler.pkl` (escalador de características)
  - `features.json` (información de las características)
  - `requirements.txt` (dependencias)
- **Variables de entorno:**
  - `PYTHON_VERSION=3.11.11` (para garantizar la compatibilidad de versiones)

## Documentación del despliegue

- **Instrucciones de instalación:**
  - El servicio se despliega automáticamente en Render al hacer push a GitHub, usando `pip install -r requirements.txt`.
  - (Esta es una caracerística principal de Render, lo cual añade facilidad al despliegue)
- **Instrucciones de configuración:**
  - Configurar "Root Directory" como `scripts/deployments` en Render.
  - Establecer la variable de entorno `PYTHON_VERSION=3.11.11`.
- **Instrucciones de uso:**
  - Enviar una solicitud de evaluación de fraude POST a la siguiente URL: `https://mlds6-fraud-detection-api.onrender.com/predict` con una transacción que esté en formato JSON.
  - Ejemplo:
    ```{"amt": 100.50, "category": "grocery_pos", ...}'
    ```
- **Instrucciones de mantenimiento:**
  - Para actualizar el modelo, reentrenarlo localmente con las mismas versiones de librerías, reemplazar `modelo_fraude_v1.pkl` y hacer push a GitHub para un nuevo despliegue automático.
  - Monitorizar los logs de Render para detectar errores o advertencias.
  - Se recomienda mantener actualizadas las dependencias y reentrenar el modelo periódicamente con nuevos datos.
  - Se recomienda utilizar una máquina con mayor poder de computo paa entrenar modelos con ponteciales mejores resultados, tales como: XGboost, RandomForest, Redes Neuronales, entre otros (Próximos pasos). 
