# execute_mysql.py
import sys
import os
# Ensure the parent directory is in the path to import config when running this script directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import pymysql
from config.databaseConfig import CONFIG

def execute_mysql_query(sql_query):
    # Vérifier si la requête commence par "select"
    if not sql_query.strip().lower().startswith("select"):
        return "❌ Erreur : Seules les requêtes commençant par 'select' sont autorisées."

    try:
        conn = pymysql.connect(
            host=CONFIG["mysql"]["host"],
            user=CONFIG["mysql"]["user"],
            password=CONFIG["mysql"]["password"],
            database=CONFIG["mysql"]["database"]
        )
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

def test_database_connection():
    try:
        conn = pymysql.connect(
            host=CONFIG["mysql"]["host"],
            user=CONFIG["mysql"]["user"],
            password=CONFIG["mysql"]["password"],
            database=CONFIG["mysql"]["database"],
            port=CONFIG["mysql"].get("port", 3306)
        )
        conn.close()
        return "✅ Connexion à la base de données réussie."
    except Exception as e:
        return f"❌ Échec de la connexion : {e}"

if __name__ == "__main__":
    print(test_database_connection())
