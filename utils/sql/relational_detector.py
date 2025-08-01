# relational_detector.py

from utils.rag.query_mistral import query_mistral

def is_relational_query(question, db_description):
    prompt = [
        {
            "role": "system",
            "content": (
                "Tu es un assistant qui détecte si une question est liée à une base de données relationnelle.\n"
                "Réponds uniquement par 'True' si la question implique une requête sur une base de données relationnelle "
                "(ex. sélection, filtrage, jointure, regroupement, comptage, etc.). Sinon, réponds par 'False'."
            )
        },
        {
            "role": "user",
            "content": (
                f"Description de la base de données : {db_description}\n"
                f"Question : {question}\n\n"
                "Est-ce une requête relationnelle ?"
            )
        }
    ]
    try:
        response = query_mistral(prompt).strip().lower()
        return "true" in response
    except Exception as e:
        return False  # En cas d'erreur, on considère que ce n'est pas une requête relationnelle
