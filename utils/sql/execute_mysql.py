# execute_mysql.py
import sys
import os
# Ensure the parent directory is in the path to import config when running this script directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import pymysql
from config.databaseConfig import CONFIG

def get_db_connection():
    return pymysql.connect(
        host=CONFIG["mysql"]["host"],
        user=CONFIG["mysql"]["user"],
        password=CONFIG["mysql"]["password"],
        database=CONFIG["mysql"]["database"],
        port=CONFIG["mysql"].get("port", 3306)
    )

def execute_mysql_query(sql_query):
    # Vérifier si la requête commence par "select"
    if not sql_query.strip().lower().startswith("select"):
        return "❌ Erreur : Seules les requêtes commençant par 'select' sont autorisées."

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)

        if cursor.description:
            rows = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
            output = " | ".join(headers) + "\n" + "-" * 50 + "\n"
            for row in rows:
                output += " | ".join(str(cell) for cell in row) + "\n"
        else:
            conn.commit()
            output = f"✅ Requête exécutée avec succès (affecté : {cursor.rowcount} lignes)."

        cursor.close()
        conn.close()
        return output.strip()

    except Exception as e:
        return f"❌ Erreur : {e}"

def format_query_result(cursor):
    headers = [desc[0] for desc in cursor.description]
    separator = " | ".join(headers) + "\n" + "-" * 50 + "\n"
    rows = cursor.fetchall()
    lines = [separator]
    for row in rows:
        lines.append(" | ".join(str(cell) for cell in row) + "\n")
    return "".join(lines)

def fetch_tables_info():
    """
    Récupère la liste de toutes les tables de la base via "SHOW TABLES;"
    puis pour chaque table, récupère sa description (DESC) et un exemple (SELECT * FROM table LIMIT 1).
    Renvoie un dictionnaire structuré avec les descriptions et exemples.
    """
    new_data = {"description": {}, "examples": {}}
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Récupérer la liste de toutes les tables
        cursor.execute("SHOW TABLES;")
        tables = [row[0] for row in cursor.fetchall()]
        for table in tables:
            try:
                desc_query = f"DESC {table};"
                cursor.execute(desc_query)
                description = format_query_result(cursor)
            except Exception as e:
                description = f"❌ Erreur pour DESC {table}: {e}"
            new_data["description"][table] = description

            try:
                select_query = f"SELECT * FROM {table} LIMIT 1;"
                cursor.execute(select_query)
                example = format_query_result(cursor)
            except Exception as e:
                example = f"❌ Erreur pour SELECT {table}: {e}"
            new_data["examples"][table] = example
        cursor.close()
        conn.close()
        return new_data
    except Exception as e:
        return {"error": f"❌ Erreur de connexion : {e}"}

def test_database_connection():
    try:
        conn = get_db_connection()
        conn.close()
        return "✅ Connexion à la base de données réussie."
    except Exception as e:
        return f"❌ Échec de la connexion : {e}"

if __name__ == "__main__":
    print(test_database_connection())
