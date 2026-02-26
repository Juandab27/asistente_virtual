🧠 **Asistente Virtual**

📌 Descripción

Asistente Virtual es una aplicación web desarrollada en Python que integra inteligencia artificial para ofrecer múltiples herramientas en una sola plataforma.

El sistema utiliza el modelo gemini-2.5-flash de Google para generar respuestas inteligentes y estructuradas en español.

La aplicación permite:

📄 Analizar textos académicos.

📚 Analizar documentos PDF.

💰 Recibir asesoría financiera personalizada.

🗓️ Crear planes de organización y productividad.

🎬 Obtener recomendaciones de películas y series.

🔗 Generar códigos QR automáticamente.

Está pensada para estudiantes, profesionales y cualquier persona que quiera apoyo académico y personal mediante inteligencia artificial.

🚀 Tecnologías Utilizadas

Python

Streamlit

Google Generative AI (Gemini 2.5 Flash)

PyPDF2

qrcode

Pillow

⚙️ Instalación
🔹 Requisitos previos

Tener Python 3.9 o superior instalado.

Tener pip instalado.

Tener una API Key de Google AI Studio.

🔑 Obtener la API Key

Ingresa a: https://aistudio.google.com

Inicia sesión con tu cuenta de Google.

Ve a la sección API Keys.

Crea una nueva API Key.

Copia la clave generada.

En el archivo backend_asistente.py, reemplaza:

genai.configure(api_key="PON-TU-API-AQUI")

Por tu clave real:

genai.configure(api_key="AIzaSyXXXXXXXXXXXX")

⚠️ Importante: No subas tu API Key real a GitHub.

📥 Clonar el repositorio
git clone https://github.com/TU_USUARIO/asistente_virtual.git
▶️ Cómo iniciar la aplicación
1️⃣ Entrar a la carpeta del proyecto
cd asistente_virtual

(Si el nombre de la carpeta es diferente, usa ese nombre).

2️⃣ Instalar dependencias

Si tienes requirements.txt:

pip install -r requirements.txt

Si no lo tienes:

pip install streamlit google-generativeai PyPDF2 qrcode Pillow
3️⃣ Ejecutar la aplicación
python -m streamlit run app.py
4️⃣ Abrir en el navegador

Ve a:

http://localhost:8501

La aplicación se ejecutará localmente en tu computadora.

🧩 Uso

Al iniciar la aplicación encontrarás un menú lateral con los siguientes módulos:

📄 Analizador de texto

📚 Analizador de PDF

💰 Asistente de finanzas

🗓️ Planificador personal

🎬 Recomendador de películas y series

🔗 Generador de código QR

Selecciona un módulo, ingresa la información solicitada y obtén el resultado generado por la inteligencia artificial.

📅 Versión
Asistente Virtual (2025) 🚀
