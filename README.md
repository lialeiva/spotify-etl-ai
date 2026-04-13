# Spotify ETL Pipeline integración con la AI

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Spotify API](https://img.shields.io/badge/Spotify-API-1DB954)
![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?logo=openai&logoColor=white)

## 📋 Descripción del Proyecto

Este proyecto implementa un **sistema completo de procesamiento ETL** (Extract, Transform, Load) que extrae datos de la API de Spotify, los transforma y limpia, y los carga en una base de datos estructurada. Como valor añadido, integra un **LLM (Large Language Model) de OpenAI** para generar análisis automáticos y detección de anomalías en los datos musicales.

### 🎯 Características principales

- **Extract**: Conexión a la API de Spotify para obtener datos de playlists, canciones, artistas y características de audio.
- **Transform**: Limpieza, normalización y enriquecimiento de datos (duración, popularidad, features de audio).
- **Load**: Almacenamiento persistente en base de datos SQLite.
- **AI Integration**: Uso de OpenAI GPT para:
  - Generar descripciones automáticas de las playlists cargadas.
  - Detectar anomalías o inconsistencias en los datos (ej: duraciones extremas, valores atípicos en popularidad).
  - Explicar patrones interesantes en lenguaje natural.

## 🏗️ Estructura del Proyecto
```
spotify-etl-ai/
│── connection/               # Módulos de conexión a APIs
│   ├── openAIConnection.py   # Conexión con OpenAI API
│   └── spotifyAPIConnection.py # Conexión con Spotify API
│
│── db/                       # Gestión de base de datos
│   └── createTable.py        # Script para creación de tablas
│
│── etl/                      # Procesos ETL
│   ├── extract.py            # Extracción de datos desde Spotify
│   ├── transform.py          # Transformación y limpieza de datos
│   └── load.py               # Carga en base de datos
│
│── llm/                      # Integración con modelos de lenguaje
│   └── spotifyAnalytics.py   # Análisis y enriquecimiento con LLM
│
├── cfg.py                    # Configuración del proyecto
├── main.py                   # Punto de entrada principal
├── requirements.txt          # Dependencias del proyecto
├── .env.production           # Variables entorno (producción) 
└── READ.me                   # Documentación auxiliar
```

## 🚀 Requisitos Previos

- Python 3.10 o superior
- Cuenta de [Spotify](https://open.spotify.com/)
- Cuenta de desarrollador en [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
- Cuenta en [OpenAI Platform](https://platform.openai.com/) con créditos o suscripción
- Pip y virtualenv (recomendado)

## 🔧 Instalación

```bash
1. Clonar el repositorio

git clone https://github.com/lialeiva/spotify-etl-ai.git
cd spotify-etl-ai

2. Crear y activar entorno virtual

python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

3. Instalar dependencias

pip install -r requirements.txt

4. Crear la base de datos
Cree una base de datos en postgres con el nombre que desee, puede crear un usuario con privilegios de administración y ponerlo como propietario de la base de datos que creó.


5. Configurar variables de entorno
Crea un archivo .env.local (para desarrollo) en la raíz del proyecto con el siguiente contenido o realiza una copia desde env.production:

OPENAI_API_KEY=
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
SPOTIFY_REDIRECT_URI=https://google.com

DB_USER=usuario propietario de la base de datos creada
DB_PASSWORD=password del db_user
DB_HOST=
DB_PORT=5432
DB_NAME=nombre de la bd creada
```

💻 Uso del Proyecto
Ejecutar el pipeline ETL completo

python main.py

Esto ejecutará secuencialmente:

- **Extract**: Obtiene datos de Spotify (played_at, artist, tracks, url).
- **Transform**: Limpia y estructura los datos.
- **Load**: Guarda los datos en la base de datos.
- **AI Analysis**: Llama a OpenAI para generar insights.

## 🖥️ Ejemplo de salida

Así verá las salidas al ejecutar el pipeline ETL:

```bash
🚀 Iniciando pipeline ETL...
📅 Procesando datos desde: 2026-04-12 01:20:52

📥 PASO 1: EXTRACT
✅ Extracted 25 registers

🔄 Transformando datos...
✅ Transformados 25 registros

       played_at               artist                                             track                                                                 url                          
2026-04-13T05:18:50.052Z      Avril Lavigne                                                                        Complicated https://open.spotify.com/artist/0p4nmQO2msCgU4IF37Wi3j
2026-04-13T05:14:19.643Z       Benson Boone                                                                   Beautiful Things https://open.spotify.com/artist/22wbnEMDvgVIAGdFeek6ET
... (más filas) ...

💾 PASO 3: LOAD
ℹ️ La tabla 'spotify_recently_playlist' ya existe, no se necesita crear
   ✅ Cargados 25 registros

🎉 Pipeline ETL completado exitosamente ✅
📊 Total de registros cargados: 25

🤖 PASO 4 LLM: GENERAR ANALISIS DE PLAY LIST

😊 Analyze mood:
Overall, the mood reads as emotionally charged and catchy...

😊 General description:
Your playlist points to...

💿 Suggest playlist name:
1. **Desamor con Guitarras y Corazón**  
2. **Pop Rock & Besos Amargos (EN/ES)**  
3. **De “Complicated” a “Algo Más”**  
4. **Serenata Alternativa para Superarlo**  
5. **Entre Takedown y Chocolate**
```

## 📊 Diagrama de flujo ETL + LLM resumido

![Flujo ETL + LLM](etl_llm_flow_summary.png)






