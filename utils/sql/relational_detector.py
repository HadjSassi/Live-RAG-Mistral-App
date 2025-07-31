# relational_detector.py

from utils.query_mistral import query_mistral


def is_relational_query(question):
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
            "content": f"Question : {question}\n\nEst-ce une requête relationnelle ?"
        }
    ]

    response = query_mistral(prompt).strip().lower()

    return "true" in response
