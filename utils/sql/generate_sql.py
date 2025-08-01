# generate_sql.py

from utils.rag.query_mistral import query_mistral

def generate_relational_query(question, table_description):
    prompt = [
        {
            "role": "system",
            "content": (
                "Tu es un expert SQL. Génère UNIQUEMENT une requête SQL basée sur la question suivante "
                "et la description de la base de données. Ne donne aucune explication, uniquement la requête."
            )
        },
        {
            "role": "user",
            "content": (
                f"Description de la base de données :\n{table_description}\n\n"
                f"Question : {question}\n\n"
                f"SQL :"
            )
        }
    ]

    response = query_mistral(prompt).strip()

    if "```" in response:
        response = response.replace("```sql", "").replace("```", "").strip()

    return response
