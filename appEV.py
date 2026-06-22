from flask import Flask, render_template, url_for
app = Flask(__name__)
import random
@app.route('/pestaña1')
def pestaña1():
    historial_eventos = [
        {"hora": "15:30:22", "coordenada": "[0,3]", "estado": "Activo"},
        {"hora": "15:31:05", "coordenada": "[2,1]", "estado": "Inactivo"},
        {"hora": "15:32:14", "coordenada": "[1,2]", "estado": "Activo"},
        {"hora": "15:33:40", "coordenada": "[3,0]", "estado": "Activo"}
    ]
    
    # DUALIDAD DE NOMBRES: Enviamos la lista tanto con el nombre 'eventos' como 'historial_eventos'
    # para que el HTML la lea sí o sí.
    return render_template('pestaña1.html', eventos=historial_eventos, historial_eventos=historial_eventos)
@app.route('/pestaña2')
# --- PESTAÑA 2: ESTADÍSTICAS Y MÉTRICAS ---
@app.route('/pestaña2')
def pestaña2():
    # 1. Creamos una matriz temporal idéntica a la de inicio para calcular sobre ella
    matriz_aux = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]
    
    # 2. Hacemos cálculos matemáticos con Python
    total_puntos = 16
    puntos_activos = sum(fila.count(1) for fila in matriz_aux)
    porcentaje_uso = (puntos_activos / total_puntos) * 100

    # 3. Empaquetamos los resultados
    datos_metricas = {
        "activos": puntos_activos,
        "porcentaje": round(porcentaje_uso, 1),
        "estado_sistema": "ÓPTIMO" if puntos_activos < 12 else "SOBRECARGADO"
    }
    
    # Se lo enviamos a pestaña2.html
    return render_template('pestaña2.html', metricas=datos_metricas)
# --- PESTAÑA 3: CONFIGURACIÓN DEL SISTEMA ---
@app.route('/pestaña3')
def pestaña3():
    # Parámetros fijos que simulan la configuración de las alertas del hardware
    config_hardware = {
        "limite_alerta": 12,
        "frecuencia_muestreo": "4 segundos",
        "version_firmware": "v2.4.1-Stable",
        "ip_servidor": "0.0.0.0 (Localhost)"
    }
    return render_template('pestaña3.html', config=config_hardware)
# --- PESTAÑA DE INICIO (MATRIZ DINÁMICA) ---
@app.route('/')
def index():
    matriz_dinamica = [
        [random.randint(0, 1) for _ in range(4)],
        [random.randint(0, 1) for _ in range(4)],
        [random.randint(0, 1) for _ in range(4)],
        [random.randint(0, 1) for _ in range(4)]
    ]
    
    # REVISA ESTA LÍNEA: Le pasamos los datos aleatorios usando los DOS nombres 
    # para asegurar que tu HTML lo encuentre de cualquier forma.
    return render_template('index.html', matriz=matriz_dinamica, matriz_dinamica=matriz_dinamica)
if __name__ == '__main__':
    # El host='0.0.0.0' le dice a Flask que sea visible para tu celular en la misma red Wi-Fi
    app.run(host='0.0.0.0', port=8080, debug=True)
