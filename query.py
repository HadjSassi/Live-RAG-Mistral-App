# query.py
from config.databaseDescription import get_full_database_info
from utils.sql.execute_mysql import execute_mysql_query
from utils.sql.generate_sql import generate_relational_query
from utils.sql.relational_detector import is_relational_query
from utils.retriever import get_relevant_chunks
from utils.query_mistral import query_mistral
import os
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.nn.modules.module")

def format_prompt(context, question):
    return [
        {"role": "system", "content": "You are a helpful assistant. Answer the question based only on the context. Toujours en francais"},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]

def handle_relational_query(question, db_description,):
    print("🔍 Détection : requête relationnelle.")
    sql = generate_relational_query(question, db_description)
    print("\n📄 Requête SQL générée :\n", sql)
    result = execute_mysql_query(sql)
    print("\n📊 Résultat de la requête :\n", result)
    context = f"Résultat SQL :\n{result}"
    messages = format_prompt(context, question)
    answer = query_mistral(messages)
    print("\n🤖 Réponse Mistral :\n", answer)

def handle_contextual_query(question):
    print("📚 Recherche contextuelle en cours...")
    chunks = get_relevant_chunks(question, top_k=10)
    context = "\n---\n".join([chunk['text'] for chunk in chunks])
    messages = format_prompt(context, question)
    answer = query_mistral(messages)
    print("\n🤖 Réponse Mistral :\n", answer)


def main():

    print("🧠 Assistant intelligent — base de données & connaissances.\n")

    while True:
        try:
            question = input("\n❓ Entrez votre question (ou 'exit' pour quitter, 'clear' pour nettoyer l'écran) : ").strip()

            if question.lower() == "exit":
                break
            if question.lower() == "clear":
                os.system("clear")
                continue

            if is_relational_query(question, get_full_database_info()):
                handle_relational_query(question, get_full_database_info())
            else:
                handle_contextual_query(question)

        except EOFError:
            print("\nFin de saisie (Ctrl+D détecté).")
            break


if __name__ == "__main__":
    main()