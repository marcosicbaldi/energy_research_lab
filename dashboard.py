import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Energy Data Dashboard", layout="wide", page_icon="📊")
st.title("📊 Dashboard Interattiva Analisi Dati Energia")

# 1. BARRA LATERALE
st.sidebar.header("Filtri di Caricamento")

data_root = Path("02_data")
FONTI_DATI = ["terna", "arera", "gse", "gme", "istat", "eurostat", "reference"]

# Gestione anni presenti
if data_root.exists():
    anni_disponibili = [f.name for f in data_root.iterdir() if f.is_dir() and f.name.isdigit()]
    if not anni_disponibili:
        anni_disponibili = ["2026"]
else:
    anni_disponibili = ["2026"]

anno_scelto = st.sidebar.selectbox("Seleziona l'Anno", sorted(anni_disponibili, reverse=True))
fonte_scelta = st.sidebar.selectbox("Seleziona la Fonte Dati", FONTI_DATI)

cartella_target = data_root / anno_scelto / fonte_scelta
st.sidebar.info(f"Cartella analizzata: `{cartella_target}`")

# 2. STRUMENTO DI EMULAZIONE DATI (Se la cartella è vuota)
files_disponibili = []
if cartella_target.exists():
    files_disponibili = [f.name for f in cartella_target.glob("*") if f.suffix in [".csv", ".xlsx", ".json"]]

if not files_disponibili:
    st.warning(f"Nessun file trovato in: {cartella_target}")
    
    # Pulsante magico per creare dati di test se sei a secco
    st.info("💡 Vuoi testare la dashboard adesso? Clicca qui sotto per generare un file di test in questa cartella.")
    if st.button("✨ Genera File di Test Simulato"):
        cartella_target.mkdir(parents=True, exist_ok=True)
        # Creiamo dati finti di produzione energetica mensile
        mesi = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
        dati_finti = pd.DataFrame({
            "Mese": mesi,
            "Consumi_GWh": np.random.randint(25000, 32000, size=12),
            "Produzione_Rinnovabile_GWh": np.random.randint(8000, 15000, size=12),
            "Prezzo_Medio_MWh": np.random.uniform(90.0, 140.0, size=12).round(2)
        })
        dati_finti.to_csv(cartella_target / "Dati_Simulati_Energia.csv", index=False)
        st.rerun() # Riavvia la pagina per leggere il nuovo file

else:
    # 3. AREA DI ANALISI ATTIVA (Quella che usa Lorenzo!)
    file_scelto = st.sidebar.selectbox("Seleziona il File", files_disponibili)
    path_file_completo = cartella_target / file_scelto

    try:
        if path_file_completo.suffix == ".csv":
            df = pd.read_csv(path_file_completo)
        elif path_file_completo.suffix == ".xlsx":
            df = pd.read_excel(path_file_completo)
        elif path_file_completo.suffix == ".json":
            df = pd.read_json(path_file_completo)

        # Indicatori veloci
        col1, col2 = st.columns(2)
        col1.metric("Dimensioni Dataset (Righe)", df.shape[0])
        col2.metric("Numero Colonne disponibili", df.shape[1])

        # Tabella Interattiva
        st.subheader("📋 Esplora il Dataset")
        st.dataframe(df, use_container_width=True) 

        # Grafici Interattivi
        st.subheader("📈 Grafici di Analisi Rapida")
        c1, c2, c3 = st.columns(3)
        with c1:
            col_x = st.selectbox("Asse X (es. Tempo/Categorie)", df.columns, index=0)
        with c2:
            # Seleziona la seconda colonna come Y di default se esiste
            default_y = 1 if len(df.columns) > 1 else 0
            col_y = st.selectbox("Asse Y (Valore metrico)", df.columns, index=default_y)
        with c3:
            tipo_grafico = st.selectbox("Stile Grafico", ["Linee", "Barre", "Dispersione"])

        # Rendering del grafico scelto
        df_chart = df.set_index(col_x)[[col_y]]
        if tipo_grafico == "Linee":
            st.line_chart(df_chart, use_container_width=True)
        elif tipo_grafico == "Barre":
            st.bar_chart(df_chart, use_container_width=True)
        elif tipo_grafico == "Dispersione":
            st.scatter_chart(df[[col_x, col_y]], use_container_width=True)

    except Exception as e:
        st.error(f"Errore nel caricamento del file: {e}")