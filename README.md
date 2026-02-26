# 🧠 Asistente Virtual

Aplicación web con Inteligencia Artificial desarrollada en Python.

El **Asistente Virtual** es una plataforma interactiva que integra múltiples herramientas impulsadas por IA en un solo entorno web intuitivo y fácil de usar.

Utiliza el modelo **Gemini 2.5 Flash** de Google para generar respuestas inteligentes, estructuradas y en español.

Está diseñada para estudiantes, profesionales y cualquier persona que necesite apoyo académico, organizacional o personal mediante Inteligencia Artificial.

---

# ✨ Funcionalidades

## 📄 Analizador de Texto Académico

* Resumen estructurado
* Idea central
* Argumentos principales
* Conceptos clave
* Preguntas para debate
* Análisis crítico

## 📚 Analizador de PDF

* Resumen automático
* Identificación del tema principal
* Comentario crítico

## 💰 Asistente de Finanzas Personales

* Diagnóstico financiero
* Plan de ahorro
* Organización de gastos

## 🗓️ Planificador Personal

* Organización por días o semanas
* Recomendaciones de productividad

## 🎬 Recomendador de Películas y Series

* Sugerencias personalizadas
* Género, año y descripción

## 🔗 Generador de Código QR

* Creación automática de códigos QR a partir de texto o enlaces

---

# 🛠️ Tecnologías Utilizadas

* Python
* Streamlit
* Google Generative AI (Gemini 2.5 Flash)
* PyPDF2
* qrcode
* Pillow

---

# 🚀 Instalación y Ejecución

## 1️⃣ Clonar el repositorio

```
git clone https://github.com/TU_USUARIO/asistente_virtual.git
```

## 2️⃣ Entrar a la carpeta del proyecto

```
cd asistente_virtual
```

## 3️⃣ Instalar dependencias

Si tienes `requirements.txt`:

```
pip install -r requirements.txt
```

Si no lo tienes:

```
pip install streamlit google-generativeai PyPDF2 qrcode Pillow
```

---

## 4️⃣ Configurar la API Key

1. Ingresa a **Google AI Studio**:
   [https://aistudio.google.com](https://aistudio.google.com)

2. Crea una nueva API Key.

3. En el archivo `backend_asistente.py`, reemplaza:

```python
genai.configure(api_key="TU_API_KEY_AQUI")
```

Por tu clave real:

```python
genai.configure(api_key="AIzaSyXXXXXXXXXXXX")
```

⚠️ **Nunca subas tu API Key real a GitHub.**

---

## 5️⃣ Ejecutar la aplicación

```
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

---

# 👨‍💻 Autor

Proyecto academico desarrollado de manera individual.

**Juan David Bermúdez**

Responsable del diseño, arquitectura, desarrollo completo del código, integración del modelo Gemini e implementación de funcionalidades de la aplicación.

---

# 📌 Versión

Asistente Virtual — 2025 🚀

---
