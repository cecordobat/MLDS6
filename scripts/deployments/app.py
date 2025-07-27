import pandas as pd
import numpy as np
import joblib
import json
from flask import Flask, request, jsonify

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
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'modelo': 'activo'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
