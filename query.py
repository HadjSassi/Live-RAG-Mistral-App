# query.py
from config.databaseDescription import get_full_database_info
from utils.rag import handle_contextual_query
from utils.sql import handle_relational_query
from utils.sql.relational_detector import is_relational_query
import os
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.nn.modules.module")

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