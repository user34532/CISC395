from src.ai_assistant import ask, rag_ask
from src.rag import build_index

def main():
    while True:
        print("\nMenu:")
        print("[6] Ask AI")
        print("[8] Search my guides")
        print("[R] Rebuild search index")
        print("[Q] Quit")

        choice = input("Choose an option: ")

        if choice == "6":
            q = input("Ask AI: ")
            print(ask(q))

        elif choice == "8":
            q = input("Ask about your guides: ")
            print(rag_ask(q))

        elif choice.upper() == "R":
            build_index()
            print("Index rebuilt.")

        elif choice.upper() == "Q":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
