import pandas as pd
import numpy as np
import joblib
import json
from flask import Flask, request, jsonify
import os

# Inicializar Flask
app = Flask(__name__)

# Cargar modelo y componentes
#model = joblib.load('modelo/modelo_fraude.pkl')
#scaler = joblib.load('modelo/scaler.pkl')
model = joblib.load('modelo_fraude.pkl')
scaler = joblib.load('scaler.pkl')

with open('features.json', 'r') as f:
    features_info = json.load(f)

# Función de predicción
def predecir_fraude(datos):
    # Convertir a DataFrame
    df = pd.DataFrame([datos])
    
    # Codificar variables categóricas
    df_encoded = pd.get_dummies(df, columns=features_info['categorical_features'])
    
    # Asegurar columnas
    for col in features_info['all_features']:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    
    # Reordenar columnas
    df_encoded = df_encoded[features_info['all_features']]
    
    # Escalar variables numéricas
    numeric_cols = features_info['numeric_features']
    df_encoded[numeric_cols] = scaler.transform(df_encoded[numeric_cols])
    
    # Predicción
    prediccion = model.predict(df_encoded)[0]
    probabilidad = model.predict_proba(df_encoded)[0][1]
    
    return int(prediccion), float(probabilidad)

# Endpoint de predicción
@app.route('/predict', methods=['POST'])
def predict():
    try:
        datos = request.json
        prediccion, probabilidad = predecir_fraude(datos)
        
        return jsonify({
            'es_fraude': prediccion,
            'probabilidad_fraude': probabilidad,
            'mensaje': 'Fraudulenta' if prediccion == 1 else 'Legítima'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Health check
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Detector de Fraude</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; max-width: 800px; }
            textarea { width: 100%; height: 150px; padding: 10px; font-family: monospace; }
            button { padding: 12px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; margin-top: 10px; font-size: 16px; }
            button:hover { background-color: #45a049; }
            #resultado { margin-top: 20px; padding: 15px; border-radius: 5px; white-space: pre-wrap; font-family: monospace; }
            .fraude { background-color: #ffebee; border-left: 6px solid #f44336; }
            .legitimo { background-color: #e8f5e9; border-left: 6px solid #4CAF50; }
            .error { background-color: #ffebee; border-left: 6px solid #f44336; color: #c62828; }
            .ejemplo { background-color: #e3f2fd; padding: 10px; margin-top: 10px; font-size: 12px; }
        </style>
    </head>
    <body>
        <h1>Detector del Fraude Transaccional - Despliegue del Módulo 6 (MLDS) UNAL - Cristhian Enrique Córdoba Trillos</h1>
        <p>Ingrese los datos de la transacción en formato JSON:</p>
        <textarea id="jsonData" placeholder='{"amt": 100.50, "category": "grocery_pos", "gender": "M", ...}'>{"amt": 100.50, "category": "grocery_pos", "gender": "M", "state": "CA", "job": "engineer", "city": "Los Angeles", "merchant": "fraud_Merchant123", "lat": 34.0522, "long": -118.2437, "city_pop": 3979576, "merch_lat": 34.0522, "merch_long": -118.2437, "day": 15, "month": 6, "hour": 14, "minute": 30, "age": 35}</textarea>
        <br>
        <button onclick="evaluarTransaccion()">Evaluar Transacción</button>
        
        <div class="ejemplo">
            <p><strong>Ejemplo de formato JSON:</strong></p>
            <code>
{"amt": 100.50, "category": "grocery_pos", "gender": "M", "state": "CA", "job": "engineer", "city": "Los Angeles", "merchant": "fraud_Merchant123", "lat": 34.0522, "long": -118.2437, "city_pop": 3979576, "merch_lat": 34.0522, "merch_long": -118.2437, "day": 15, "month": 6, "hour": 14, "minute": 30, "age": 35}
            </code>
        </div>

        <div id="resultado"></div>

        <script>
            async function evaluarTransaccion() {
                const jsonString = document.getElementById('jsonData').value;
                const divResultado = document.getElementById('resultado');

                if (!jsonString.trim()) {
                    divResultado.innerHTML = 'Por favor, ingrese datos en formato JSON.';
                    divResultado.className = 'error';
                    return;
                }

                try {
                    // Intentar parsear el JSON para validar
                    const datosTransaccion = JSON.parse(jsonString);

                    // Enviar solicitud POST a /predict
                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(datosTransaccion)
                    });

                    if (!response.ok) {
                        const errorText = await response.text();
                        throw new Error(`Error HTTP ${response.status}: ${errorText}`);
                    }

                    const resultado = await response.json();

                    // Mostrar resultado formateado
                    const mensajeResultado = `Es Fraude: ${resultado.es_fraude === 1 ? 'Sí' : 'No'}
Probabilidad: ${(resultado.probabilidad_fraude * 100).toFixed(2)}%
Mensaje: ${resultado.mensaje}`;

                    divResultado.textContent = mensajeResultado;
                    divResultado.className = resultado.es_fraude === 1 ? 'fraude' : 'legitimo';

                } catch (error) {
                    console.error('Error:', error);
                    let mensajeError = `Error al evaluar la transacción: ${error.message}`;
                    if (error instanceof SyntaxError) {
                        mensajeError = 'Error: El texto ingresado no es un JSON válido. Por favor, revise el formato.';
                    }
                    divResultado.textContent = mensajeError;
                    divResultado.className = 'error';
                }
            }

            // Permitir enviar con Ctrl+Enter
            document.getElementById('jsonData').addEventListener('keydown', function(e) {
                if (e.ctrlKey && e.key === 'Enter') {
                    evaluarTransaccion();
                }
            });
        </script>
    </body>
    </html>
    '''


if __name__ == '__main__':
    # Asegúrate de que esta línea esté después de las importaciones
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
