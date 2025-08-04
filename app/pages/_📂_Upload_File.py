import streamlit as st
import os

extensions = ["txt"]

def save_uploaded_file(uploaded_file, path):
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Fichier sauvegardé dans {path}")


st.title("Uploader un fichier")

uploaded_file = st.file_uploader("Choisissez un fichier", type=extensions)
if uploaded_file is not None:
    # Créer le dossier 'documents' s'il n'existe pas
    documents_folder = os.path.join(os.getcwd(), "documents")
    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)

    file_path = os.path.join(documents_folder, uploaded_file.name)
    save_uploaded_file(uploaded_file, file_path)