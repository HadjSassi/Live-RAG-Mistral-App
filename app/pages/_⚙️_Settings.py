import streamlit as st
from config import databaseConfig

# Obtenir la configuration initiale
config = databaseConfig.CONFIG

with st.form("config_form"):
    # Sélection de l'engine
    engine_options = ["mysql", "postgresql", "sqlite"]
    engine_index = engine_options.index(config["engine"]) if config["engine"] in engine_options else 0
    engine = st.selectbox("Choisir le moteur de base de données", engine_options, index=engine_index)

    engine_config = config.get(engine, {})

    # Affichage des champs selon le moteur sélectionné
    if engine == "sqlite":
        db_path = st.text_input("Chemin de la base de données", engine_config.get("db_path", ""))
    elif engine == "mysql":
        host = st.text_input("Hôte", engine_config.get("host", ""))
        user = st.text_input("Utilisateur", engine_config.get("user", ""))
        password = st.text_input("Mot de passe", engine_config.get("password", ""), type="password")
        database = st.text_input("Nom de la base", engine_config.get("database", ""))
        port = st.number_input("Port", value=engine_config.get("port", 3306))
    elif engine == "postgresql":
        host = st.text_input("Hôte", engine_config.get("host", ""))
        user = st.text_input("Utilisateur", engine_config.get("user", ""))
        password = st.text_input("Mot de passe", engine_config.get("password", ""), type="password")
        database = st.text_input("Nom de la base", engine_config.get("database", ""))

    submitted = st.form_submit_button("Soumettre")
    if submitted:
        st.success("Configuration mise à jour !")