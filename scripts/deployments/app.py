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
@app.route('/')
def index():
    # Puedes devolver directamente HTML o usar un motor de plantillas como Jinja2
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Detector de Fraude</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            input, select { margin: 5px 0; padding: 8px; width: 200px; }
            button { padding: 10px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; margin-top: 10px; }
            #resultado { margin-top: 20px; padding: 15px; border-radius: 5px; }
            .fraude { background-color: #ffdddd; border-left: 6px solid #f44336; }
            .legitimo { background-color: #ddffdd; border-left: 6px solid #4CAF50; }
        </style>
    </head>
    <body>
        <h1>Detector de Fraude en Transacciones</h1>
        <form id="formularioTransaccion">
            <!-- Campos para los datos de la transacción -->
            <label for="amt">Monto (amt):</label><br>
            <input type="number" id="amt" name="amt" step="0.01" required><br>

            <label for="category">Categoría (category):</label><br>
            <select id="category" name="category" required>
                <option value="grocery_pos">Grocery (POS)</option>
                <option value="shopping_net">Shopping (Online)</option>
                <option value="gas_transport">Gas/Transport</option>
                <option value="food_dining">Food/Dining</option>
                <option value="entertainment">Entertainment</option>
                <!-- Agrega más opciones según tu dataset -->
            </select><br>

            <label for="gender">Género (gender):</label><br>
            <select id="gender" name="gender" required>
                <option value="M">Masculino</option>
                <option value="F">Femenino</option>
            </select><br>

            <label for="state">Estado (state):</label><br>
            <input type="text" id="state" name="state" maxlength="2" required><br>

            <label for="job">Ocupación (job):</label><br>
            <input type="text" id="job" name="job" required><br>

            <label for="city">Ciudad (city):</label><br>
            <input type="text" id="city" name="city" required><br>

            <label for="merchant">Comerciante (merchant):</label><br>
            <input type="text" id="merchant" name="merchant" required><br>

            <label for="lat">Latitud Cliente (lat):</label><br>
            <input type="number" id="lat" name="lat" step="0.0001" required><br>

            <label for="long">Longitud Cliente (long):</label><br>
            <input type="number" id="long" name="long" step="0.0001" required><br>

            <label for="city_pop">Población Ciudad (city_pop):</label><br>
            <input type="number" id="city_pop" name="city_pop" required><br>

            <label for="merch_lat">Latitud Comerciante (merch_lat):</label><br>
            <input type="number" id="merch_lat" name="merch_lat" step="0.0001" required><br>

            <label for="merch_long">Longitud Comerciante (merch_long):</label><br>
            <input type="number" id="merch_long" name="merch_long" step="0.0001" required><br>

            <label for="day">Día (day):</label><br>
            <input type="number" id="day" name="day" min="1" max="31" required><br>

            <label for="month">Mes (month):</label><br>
            <input type="number" id="month" name="month" min="1" max="12" required><br>

            <label for="hour">Hora (hour):</label><br>
            <input type="number" id="hour" name="hour" min="0" max="23" required><br>

            <label for="minute">Minuto (minute):</label><br>
            <input type="number" id="minute" name="minute" min="0" max="59" required><br>

            <label for="age">Edad (age):</label><br>
            <input type="number" id="age" name="age" min="10" max="90" required><br>

            <button type="submit">Evaluar Transacción</button>
        </form>
        <div id="resultado"></div>

        <script>
            document.getElementById('formularioTransaccion').addEventListener('submit', async function(e) {
                e.preventDefault(); // Evitar envío normal del formulario

                // Recopilar datos del formulario
                const formData = new FormData(this);
                const datosTransaccion = {};
                for (const [key, value] of formData.entries()) {
                    // Intentar convertir a número si es posible, de lo contrario dejar como string
                    datosTransaccion[key] = isNaN(value) || value === '' ? value : Number(value);
                }

                try {
                    // Enviar solicitud POST a /predict
                    const response = await fetch('/predict', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(datosTransaccion)
                    });

                    if (!response.ok) {
                        throw new Error(`Error HTTP: ${response.status}`);
                    }

                    const resultado = await response.json();

                    // Mostrar resultado
                    const divResultado = document.getElementById('resultado');
                    divResultado.innerHTML = `
                        <h3>Resultado de la Predicción:</h3>
                        <p><strong>Es Fraude:</strong> ${resultado.es_fraude === 1 ? 'Sí' : 'No'}</p>
                        <p><strong>Probabilidad:</strong> ${(resultado.probabilidad_fraude * 100).toFixed(2)}%</p>
                        <p><strong>Mensaje:</strong> ${resultado.mensaje}</p>
                    `;
                    // Aplicar estilo según el resultado
                    divResultado.className = resultado.es_fraude === 1 ? 'fraude' : 'legitimo';

                } catch (error) {
                    console.error('Error:', error);
                    document.getElementById('resultado').innerHTML = `<p style="color:red;">Error al evaluar la transacción: ${error.message}</p>`;
                    document.getElementById('resultado').className = '';
                }
            });
        </script>
    </body>
    </html>
    '''

# ... (tu código existente para /predict y /health) ...

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
