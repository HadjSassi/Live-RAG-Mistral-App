import streamlit as st
import json
import os
from config import databaseConfig
from utils.sql.execute_mysql import test_database_connection  # nouvel import

config = databaseConfig.CONFIG

# todo make an abstration for the database connection
#engine_options = ["mysql", "postgresql", "sqlite"]
engine_options = ["mysql"]

if "engine" not in st.session_state:
    st.session_state.engine = config.get("engine", "mysql")

selected_engine = st.selectbox(
    "Choisir le moteur de base de données",
    engine_options,
    index=engine_options.index(st.session_state.engine)
)
st.session_state.engine = selected_engine

with st.form("config_form"):
    if selected_engine == "sqlite":
        db_path = st.text_input("Chemin de la base de données", config.get("sqlite", {}).get("db_path", ""))
    elif selected_engine == "mysql":
        host = st.text_input("Hôte", config.get("mysql", {}).get("host", ""))
        user = st.text_input("Utilisateur", config.get("mysql", {}).get("user", ""))
        password = st.text_input("Mot de passe", config.get("mysql", {}).get("password", ""), type="password")
        database = st.text_input("Nom de la base", config.get("mysql", {}).get("database", ""))
        port = st.number_input("Port", value=config.get("mysql", {}).get("port", 3306))
    elif selected_engine == "postgresql":
        host = st.text_input("Hôte", config.get("postgresql", {}).get("host", ""))
        user = st.text_input("Utilisateur", config.get("postgresql", {}).get("user", ""))
        password = st.text_input("Mot de passe", config.get("postgresql", {}).get("password", ""), type="password")
        database = st.text_input("Nom de la base", config.get("postgresql", {}).get("database", ""))
        port = st.number_input("Port", value=config.get("mysql", {}).get("port", 5432))

    submitted = st.form_submit_button("Soumettre")
    if submitted:
        new_config = {"engine": selected_engine}
        if selected_engine == "sqlite":
            new_config["sqlite"] = {"db_path": db_path}
        elif selected_engine == "mysql":
            new_config["mysql"] = {
                "host": host,
                "user": user,
                "password": password,
                "database": database,
                "port": port
            }
        elif selected_engine == "postgresql":
            new_config["postgresql"] = {
                "host": host,
                "user": user,
                "password": password,
                "database": database
            }
        config_file_path = os.path.join(os.path.dirname(databaseConfig.__file__), "databaseConfig.json")
        with open(config_file_path, "w") as f:
            json.dump(new_config, f, indent=2)
        st.success("Configuration mise à jour !")

# Nouveau bouton en dessous du formulaire pour tester la connexion
if st.button("Tester la connexion"):
    result = test_database_connection()
    if result.startswith("✅"):
        st.success(result)
    else:
        st.error(result)