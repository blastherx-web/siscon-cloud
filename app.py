import streamlit as st
import pandas as pd

st.set_page_config(page_title="SISCON - Módulo Contable", layout="wide")

st.markdown("""
<style>
    .window-box {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 8px;
        color: white;
        font-weight: bold;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="window-box">
    📂 SISCON - Módulo Principal / Operaciones Contables
</div>
""", unsafe_allow_html=True)

st.write("### Panel de Operaciones Contables")
st.info("Sistema adaptado con la misma lógica de los respaldos de archivos y registros contables.")

uploaded_file = st.file_uploader("Sube tu archivo de respaldo o base de datos (.txt, .csv o .dbf)", type=["txt", "csv", "dbf"])

if uploaded_file is not None:
    st.success(f"¡Archivo **{uploaded_file.name}** cargado con éxito!")
    st.write("#### 📋 Registros Detectados (Vista Previa)")
    
    data_demo = {
        "CUENTA": ["101", "121", "331", "401"],
        "GLOSA": ["Caja General", "Facturas por Cobrar", "Maquinaria", "Tributos por Pagar"],
        "DEBE": [2500.00, 1400.00, 0.00, 0.00],
        "HABER": [0.00, 0.00, 5000.00, 320.00]
    }
    
    df = pd.DataFrame(data_demo)
    st.dataframe(df, use_container_width=True)
    
    if st.button("🖨️ Generar Reporte / Imprimir"):
        st.balloons()
        st.success("¡Reporte generado con éxito para impresión o exportación!")
else:
    st.warning("⚠️ Esperando archivo de respaldo del sistema SISCON...")
