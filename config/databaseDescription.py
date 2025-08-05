import json
import os

def load_description_from_json():
    base_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_path, 'databaseDescription.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        # Ignorer les lignes qui commencent par "\#"
        lines = [line for line in f if not line.strip().startswith('#')]
        json_string = ''.join(lines)
        return json.loads(json_string)

DATABASE = load_description_from_json()

def get_full_database_info():
    info = "Base de données:\n\n"
    for table, desc in DATABASE["description"].items():
        info += f"Table {table}:\n{desc}\n\n"
    info += "Exemples:\n\n"
    for table, example in DATABASE["examples"].items():
        info += f"Table {table}:\n{example}\n\n"
    return info

def update_database_description(new_data):
    """
    Récupère les nouvelles descriptions et exemples via fetch_tables_info
    et met à jour le fichier databaseDescription.json.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_path, 'databaseDescription.json')
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2)
        return "Mise à jour de databaseDescription.json réussie."
    except Exception as e:
        return f"Erreur lors de la mise à jour : {e}"