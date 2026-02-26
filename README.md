# 🧠 Asistente Virtual

<p align="center">
Aplicación web con Inteligencia Artificial desarrollada en Python  
</p>

---

## 📖 Descripción

**Asistente Virtual** es una aplicación web interactiva que integra múltiples herramientas impulsadas por inteligencia artificial en una sola plataforma.

Utiliza el modelo **Gemini 2.5 Flash** de Google para generar respuestas inteligentes, estructuradas y en español.

Está diseñada para estudiantes, profesionales y cualquier persona que quiera apoyo académico y personal mediante IA.

---

## ✨ Funcionalidades

* 📄 **Analizador de texto académico**

  * Resumen estructurado
  * Idea central
  * Argumentos principales
  * Conceptos clave
  * Preguntas para debate
  * Análisis crítico

* 📚 **Analizador de PDF**

  * Resumen automático
  * Identificación de tema principal
  * Comentario crítico

* 💰 **Asistente de finanzas personales**

  * Diagnóstico financiero
  * Plan de ahorro
  * Organización de gastos

* 🗓️ **Planificador personal**

  * Organización por días o semanas
  * Recomendaciones de productividad

* 🎬 **Recomendador de películas y series**

  * Sugerencias personalizadas
  * Género, año y descripción

* 🔗 **Generador de código QR**

  * Creación automática de códigos QR a partir de texto o enlaces

---

## 🛠️ Tecnologías Utilizadas

* Python
* Streamlit
* Google Generative AI (Gemini 2.5 Flash)
* PyPDF2
* qrcode
* Pillow

---

# 🚀 Instalación y Ejecución

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/asistente_virtual.git
```

---

## 2️⃣ Entrar a la carpeta del proyecto

```bash
cd asistente_virtual
```

---

## 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

Si no tienes `requirements.txt`:

```bash
pip install streamlit google-generativeai PyPDF2 qrcode Pillow
```

---

## 4️⃣ Configurar la API Key

1. Ve a: [https://aistudio.google.com](https://aistudio.google.com)
2. Crea una nueva API Key.
3. En el archivo `backend_asistente.py`, reemplaza:

```python
genai.configure(api_key="TU_API_KEY_AQUI")
```

Por tu clave real:

```python
genai.configure(api_key="AIzaSyXXXXXXXXXXXX")
```

⚠️ No subas tu API Key real a GitHub.

---

## 5️⃣ Ejecutar la aplicación

```bash
python -m streamlit run app.py
```

Luego abre en tu navegador:

```
http://localhost:8501
```

---

# 🧩 Cómo usar la aplicación

1. Ejecuta el proyecto.
2. Selecciona un módulo en el menú lateral.
3. Ingresa la información solicitada.
4. Haz clic en el botón correspondiente.
5. Obtén el resultado generado por la IA.


# 📌 Versión

**Asistente Virtual — 2025** 🚀

