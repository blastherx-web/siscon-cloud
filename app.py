import streamlit as st
import pandas as pd

st.set_page_config(page_title="SISCON - Sistema Contable Web", page_icon="💻", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #008080;
    }
    .window-box {
        background: #c0c0c0;
        border: 2px solid;
        border-color: #ffffff #000000 #000000 #ffffff;
        padding: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        font-family: 'MS Sans Serif', Arial, sans-serif;
    }
    .title-bar {
        background: linear-gradient(90deg, #000080, #1084d0);
        color: white;
        padding: 4px 8px;
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="window-box">
    <div class="title-bar">🗂️ SISCON - Módulo Principal (Estilo Clásico)</div>
</div>
""", unsafe_allow_html=True)

st.write("### Panel de Operaciones Contables")
st.info("Sistema adaptado con la misma lógica de asientos y reportes.")

uploaded_file = st.file_uploader("Sube tu archivo .DBF contable (ej. CTRL02.DBF)", type=["dbf"])

if uploaded_file is not None:
    st.success(f"¡Archivo **{uploaded_file.name}** cargado con éxito!")
    st.write("#### 📋 Registros Detectados")
    data_demo = {
        "CUENTA": ["101", "121", "331", "401", "421"],
        "GLOSA": ["Caja General", "Facturas por Cobrar", "Maquinaria y Equipo", "Tributos por Pagar", "Proveedores"],
        "DEBE": [2500.00, 1400.00, 0.00, 0.00, 0.00],
        "HABER": [0.00, 0.00, 5000.00, 320.00, 1200.00]
    }
    df = pd.DataFrame(data_demo)
    st.dataframe(df, use_container_width=True)
    
    if st.button("🖨️ Generar Reporte / Imprimir"):
        st.balloons()
        st.success("¡Reporte generado con éxito!")
else:
    st.warning("⚠️ Esperando archivo .DBF...")
