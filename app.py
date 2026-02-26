
import streamlit as st
import tempfile

from backend_asistente import (
    analizar_texto,
    analizar_pdf,
    asistente_finanzas,
    planificador,
    generar,
    recomendar_pelis_series,
)

st.set_page_config(page_title="Asistente Virtual", layout="wide")

st.title("🧠 Asistente Virtual")
st.write("")

st.sidebar.title("Menú de módulos")
opcion = st.sidebar.radio(
    "Selecciona un módulo:",
    [
        "Analizador de texto",
        "Analizador de PDF",
        "Asistente de finanzas",
        "Planificador personal",
        "Recomendador de películas/series",
        "Generador de código QR",
    ],
)

if opcion == "Analizador de texto":
    st.subheader("📄 Analizador de texto")
    texto = st.text_area("Pega aquí el texto:", height=250)
    if st.button("Analizar texto"):
        if texto.strip():
            with st.spinner("Analizando..."):
                resultado = analizar_texto(texto)
            st.markdown("### Resultado")
            st.write(resultado)
        else:
            st.warning("Ingresa un texto primero.")
	

elif opcion == "Analizador de PDF":
    st.subheader("📚 Analizador de PDF")
    archivo_pdf = st.file_uploader("Sube un PDF:", type=["pdf"])
    if archivo_pdf is not None and st.button("Analizar PDF"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(archivo_pdf.read())
            ruta_temporal = tmp.name
        with st.spinner("Analizando PDF..."):
            resultado = analizar_pdf(ruta_temporal)
        st.markdown("### Resultado")
        st.write(resultado)
        st.download_button(
            "Descargar análisis",
            resultado,
            file_name="analisis_texto.txt"
        )
elif opcion == "Asistente de finanzas":
    st.subheader("💰 Asistente de finanzas")
    instruccion = st.text_area("Escribe tu situación:", height=200)
    if st.button("Generar recomendación"):
        if instruccion.strip():
            with st.spinner("Generando..."):
                resultado = asistente_finanzas(instruccion)
            st.markdown("### Recomendación")
            st.write(resultado)
        st.download_button(
            "Descargar análisis",
            resultado,
            file_name="analisis_texto.txt"
        )
elif opcion == "Planificador personal":
    st.subheader("🗓️ Planificador")
    instruccion = st.text_area("¿Qué necesitas planear?", height=200)
    if st.button("Crear plan"):
        if instruccion.strip():
            with st.spinner("Creando plan..."):
                resultado = planificador(instruccion)
            st.markdown("### Plan generado")
            st.write(resultado)
        st.download_button(
            "Descargar análisis",
            resultado,
            file_name="analisis_texto.txt"
        )
elif opcion == "Recomendador de películas/series":
    st.subheader("🎬 Recomendador")
    instruccion = st.text_area("¿Qué te gusta ver?", height=200)
    if st.button("Recomendar"):
        if instruccion.strip():
            with st.spinner("Buscando..."):
                resultado = recomendar_pelis_series(instruccion)
            st.markdown("### Recomendaciones")
            st.write(resultado)
        st.download_button(
            "Descargar análisis",
            resultado,
            file_name="analisis_texto.txt"
        )
elif opcion == "Generador de código QR":
    st.subheader("🔗 Generador de QR")
    contenido = st.text_input("Texto o enlace:")
    if st.button("Generar QR"):
        if contenido.strip():
            with st.spinner("Generando QR..."):
                archivo = generar(contenido)
            st.image(archivo, caption="Código QR generado")

st.markdown("""
<hr>
<p style='text-align:center; color:gray;'>
Asistente Virtual (2025)
</p>
""", unsafe_allow_html=True)

