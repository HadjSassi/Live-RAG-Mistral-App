from utils.rag.query_mistral import get_mistral_response
from utils.sql.execute_mysql import execute_mysql_query
from utils.sql.generate_sql import generate_relational_query


def handle_relational_query(question, db_description,):
    print("🔍 Détection : requête relationnelle.")
    sql = generate_relational_query(question, db_description)
    print("\n📄 Requête SQL générée :\n", sql)
    result = execute_mysql_query(sql)
    print("\n📊 Résultat de la requête :\n", result)
    context = f"Résultat SQL :\n{result}"
    return get_mistral_response(context, question)