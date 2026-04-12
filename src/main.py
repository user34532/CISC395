from models import Destination
from storage import load_trips, save_trips


def main():
    trips = load_trips()

    while True:
        print("\n=== Trip Notes ===")
        print("[1] Add destination")
        print("[2] View all destinations")
        print("[3] Search by country")
        print("[4] Add note to a destination")
        print("[5] Quit")
        print("[6] Ask AI")
        print("[7] Generate Trip Briefing")
        print("[8] Mark as Visited")
        print("[9] Wishlist / Visited Stats")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter destination name: ")
            country = input("Enter country: ")
            budget = float(input("Enter budget: "))
            dest = Destination(name, country, budget)
            trips.add(dest)
            save_trips(trips)
            print("Destination added.")

        elif choice == "2":
            all_trips = trips.get_all()
            if not all_trips:
                print("No destinations found.")
            for i, trip in enumerate(all_trips):
                status = "Visited" if trip.visited else "Wishlist"
                print(f"{i}. {trip.name} ({trip.country}) - ${trip.budget} [{status}]")
                if trip.notes:
                    for note in trip.notes:
                        print(f"   - {note}")

        elif choice == "3":
            country = input("Enter country to search: ")
            results = trips.search_by_country(country)
            if not results:
                print("No matches found.")
            for trip in results:
                print(f"{trip.name} ({trip.country}) - ${trip.budget}")

        elif choice == "4":
            all_trips = trips.get_all()
            for i, trip in enumerate(all_trips):
                print(f"{i}. {trip.name}")
            index = int(input("Choose destination index: "))
            note = input("Enter note: ")
            trips.get_by_index(index).add_note(note)
            save_trips(trips)
            print("Note added.")

        elif choice == "5":
            print("Goodbye!")
            break

        elif choice == "6":
            question = input("Ask a travel question: ")

            print("calling ai...")

            try:
                from ai_assistant import ask
                response = ask(question)
                print("done calling ai")
            except Exception as e:
                print("ERROR calling AI:", e)
                continue

            print("\nAI Response:")
            print(response)

            save = input("\nSave this as a note? (y/n): ")

            if save.lower() == "y":
                all_trips = trips.get_all()

                if not all_trips:
                    print("No destinations available.")
                else:
                    for i, trip in enumerate(all_trips):
                        print(f"{i}. {trip.name}")

                    index = int(input("Choose destination index: "))
                    trips.get_by_index(index).add_note(response)
                    save_trips(trips)

                    print("Saved to trip notes!")

        elif choice == "7":
            all_trips = trips.get_all()

            if not all_trips:
                print("No destinations available.")
            else:
                for i, trip in enumerate(all_trips):
                    print(f"{i}. {trip.name} ({trip.country})")

                index = int(input("Choose destination index: "))
                dest = trips.get_by_index(index)

                from ai_assistant import generate_trip_briefing

                print("\nGenerating trip briefing...\n")

                overview, packing = generate_trip_briefing(
                    dest.name,
                    dest.country,
                    dest.notes
                )

                print("Overview:")
                print(overview)

                print("\nPacking list:")
                print(packing)

        elif choice == "8":
            all_trips = trips.get_all()
            for i, trip in enumerate(all_trips):
                print(f"{i}. {trip.name}")
            index = int(input("Choose destination index: "))
            trips.mark_visited(index)
            save_trips(trips)
            print("Marked as visited.")

        elif choice == "9":
            visited = trips.get_visited()
            wishlist = trips.get_wishlist()

            print(f"Visited: {len(visited)}")
            for trip in visited:
                print(f" - {trip.name}")

            print(f"\nWishlist: {len(wishlist)}")
            for trip in wishlist:
                print(f" - {trip.name}")

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()