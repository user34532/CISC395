def main():
    while True:
        print("\nMenu:")
        print("[10] AI Travel Agent")
        print("[0] Exit")

        choice = input("Enter choice: ")

        if choice == "10":
            from tools import run_agent
            question = input("Ask the AI Travel Agent: ")
            run_agent(question)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
