import streamlit as st
import json
import os
from config import databaseConfig

config = databaseConfig.CONFIG

with st.form("config_form"):
    # Sélection de l'engine
    engine_options = ["mysql", "postgresql", "sqlite"]
    engine_index = engine_options.index(config.get("engine", "mysql")) if config.get("engine") in engine_options else 0
    engine = st.selectbox("Choisir le moteur de base de données", engine_options, index=engine_index)

    # Affichage des champs selon le moteur sélectionné
    if engine == "sqlite":
        db_path = st.text_input("Chemin de la base de données", config.get("sqlite", {}).get("db_path", ""))
    elif engine == "mysql":
        host = st.text_input("Hôte", config.get("mysql", {}).get("host", ""))
        user = st.text_input("Utilisateur", config.get("mysql", {}).get("user", ""))
        password = st.text_input("Mot de passe", config.get("mysql", {}).get("password", ""), type="password")
        database = st.text_input("Nom de la base", config.get("mysql", {}).get("database", ""))
        port = st.number_input("Port", value=config.get("mysql", {}).get("port", 3306))
    elif engine == "postgresql":
        host = st.text_input("Hôte", config.get("postgresql", {}).get("host", ""))
        user = st.text_input("Utilisateur", config.get("postgresql", {}).get("user", ""))
        password = st.text_input("Mot de passe", config.get("postgresql", {}).get("password", ""), type="password")
        database = st.text_input("Nom de la base", config.get("postgresql", {}).get("database", ""))

    submitted = st.form_submit_button("Soumettre")

    if submitted:
        # Recréation de la configuration en fonction du moteur sélectionné
        new_config = {"engine": engine}
        if engine == "sqlite":
            new_config["sqlite"] = {"db_path": db_path}
        elif engine == "mysql":
            new_config["mysql"] = {
                "host": host,
                "user": user,
                "password": password,
                "database": database,
                "port": port
            }
        elif engine == "postgresql":
            new_config["postgresql"] = {
                "host": host,
                "user": user,
                "password": password,
                "database": database
            }

        # Détermine le chemin du fichier JSON de configuration
        config_file_path = os.path.join(os.path.dirname(databaseConfig.__file__), "databaseConfig.json")
        # Écriture de la nouvelle configuration dans le fichier JSON
        with open(config_file_path, "w") as f:
            json.dump(new_config, f, indent=2)
        st.success("Configuration mise à jour !")