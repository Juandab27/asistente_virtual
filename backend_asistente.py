
import google.generativeai as genai
import PyPDF2
import qrcode

# =========================
# CONFIGURACIÓN GEMINI
# =========================
# IMPORTANTE: pon aquí TU API KEY
genai.configure(api_key="PON-TU-API-AQUI")

model = genai.GenerativeModel("gemini-2.5-flash")

# =========================
# PROMPTS
# =========================

academic_prompt = """
Eres un asistente académico experto en análisis de textos universitarios.

Tu tarea es:
1. Hacer un resumen claro y estructurado del texto.
2. Identificar la idea central del autor.
3. Extraer los argumentos principales.
4. Señalar los conceptos o términos clave.
5. Proponer 5 preguntas para un conversatorio o debate.
6. Hacer un breve análisis crítico final (2–3 párrafos).

Usa un lenguaje académico pero claro; escribe en español.
"""


pdf_prompt = """
Eres un asistente académico especializado en análisis de documentos en PDF.

A partir del texto extraído del PDF debes:
1. Resumir el contenido.
2. Identificar el tema principal.
3. Señalar los puntos o secciones más importantes.
4. Destacar conceptos clave.
5. Hacer un breve comentario crítico final.

Responde en español, de forma clara y ordenada.
"""


finanzas_prompt = """
Eres un asesor financiero personal.

Con la información del usuario debes:
1. Hacer un diagnóstico sencillo de su situación (ingresos, gastos, deudas, metas).
2. Proponer un plan de organización financiera.
3. Definir un plan de ahorro (corto, mediano y largo plazo).
4. Dar recomendaciones prácticas para reducir gastos y evitar deudas innecesarias.
5. Si es posible, incluir un ejemplo numérico aproximado.

No uses lenguaje técnico complicado; explica en español claro y cercano.
"""


planner_prompt = """
Eres un planificador experto en organización personal, estudio y productividad.

A partir de lo que diga el usuario debes:
1. Hacer un resumen del objetivo principal.
2. Identificar tareas o actividades clave.
3. Organizar un plan por días, semanas o pasos (según corresponda).
4. Dar recomendaciones para mantener la disciplina y evitar la procrastinación.
5. Terminar con un pequeño mensaje motivador.

Responde siempre en español, con formato ordenado (listas, apartados, etc.).
"""


qr_prompt = """
Eres un asistente que limpia y prepara contenido para un código QR.

Tareas:
- Recibir el texto del usuario (puede ser un enlace, un mensaje, datos de contacto, etc.).
- Limpiar espacios innecesarios.
- Corregir si hay errores obvios en la URL (si aplica).
- Devolver SOLO el contenido final que debe ir dentro del QR, sin explicaciones extra.

Muy importante: tu respuesta debe ser ÚNICAMENTE el contenido limpio.
"""


recomendador_prompt = """
Eres un recomendador experto de películas y series.

Con base en lo que diga el usuario:
- Sugiere entre 5 y 7 títulos.
- Indica para cada uno:
  - Si es PELÍCULA o SERIE.
  - Género principal.
  - Año aproximado de estreno.
  - Duración aproximada (películas) o cantidad de episodios/temporadas (series).
  - Breve descripción en 2–3 líneas.

Si el usuario menciona géneros, estados de ánimo, plataformas o actores, tenlos en cuenta.
Responde en español, en formato de lista con viñetas.
"""


def leer_pdf(ruta_pdf: str) -> str:
    with open(ruta_pdf, "rb") as archivo:
        lector = PyPDF2.PdfReader(archivo)
        texto = ""
        for pagina in lector.pages:
            extraido = pagina.extract_text()
            if extraido:
                texto += extraido + "\n"
    return texto

def analizar_texto(texto: str) -> str:
    prompt = f"{academic_prompt}\n\nTexto a analizar:\n\"\"\"\n{texto}\n\"\"\"\n\nResponde ahora:"
    respuesta = model.generate_content(prompt)
    return respuesta.text.strip()

def analizar_pdf(ruta_pdf: str) -> str:
    texto = leer_pdf(ruta_pdf)
    if not texto.strip():
        return "No se pudo extraer texto del PDF. Verifica que no sea un PDF escaneado como imagen."
    prompt = f"{pdf_prompt}\n\nContenido extraído del PDF:\n\"\"\"\n{texto}\n\"\"\"\n\nResponde ahora:"
    respuesta = model.generate_content(prompt)
    return respuesta.text.strip()

def asistente_finanzas(instruccion: str) -> str:
    prompt = f"{finanzas_prompt}\n\nInformación del usuario:\n\"\"\"\n{instruccion}\n\"\"\"\n\nGenera ahora el análisis y el plan:"
    respuesta = model.generate_content(prompt)
    return respuesta.text.strip()

def planificador(instruccion: str) -> str:
    prompt = f"{planner_prompt}\n\nContexto del usuario:\n\"\"\"\n{instruccion}\n\"\"\"\n\nCrea el plan detallado:"
    respuesta = model.generate_content(prompt)
    return respuesta.text.strip()

def generar(contenido: str) -> str:
    prompt = f"{qr_prompt}\n\nContenido original del usuario:\n\"\"\"\n{contenido}\n\"\"\"\n\nResponde solo con el contenido limpio:"
    respuesta = model.generate_content(prompt)
    qr_data = respuesta.text.strip()
    img = qrcode.make(qr_data)
    filename = "codigo_qr.png"
    img.save(filename)
    return filename

def recomendar_pelis_series(instruccion: str) -> str:
    prompt = f"{recomendador_prompt}\n\nPreferencias del usuario:\n\"\"\"\n{instruccion}\n\"\"\"\n\nRecomendaciones:"
    respuesta = model.generate_content(prompt)
    return respuesta.text.strip()
