def library_system():
    library = {}  

    while True:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book by ID")
        print("4. Update Book Title")
        print("5. Display All Books")
        print("6. Count Total Books")
        print("7. Check if Book Title Exists")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            library[book_id] = title
            print("Book added successfully!")

        elif choice == 2:
            book_id = input("Enter Book ID to remove: ")
            if book_id in library:
                del library[book_id]
                print("Book removed successfully!")
            else:
                print("Book ID not found!")

        elif choice == 3:
            book_id = input("Enter Book ID to search: ")
            if book_id in library:
                print("Book Found:", library[book_id])
            else:
                print("Book ID not found!")

        elif choice == 4:
            book_id = input("Enter Book ID to update: ")
            if book_id in library:
                new_title = input("Enter new title: ")
                library[book_id] = new_title
                print("Book title updated!")
            else:
                print("Book ID not found!")

        elif choice == 5:
            if library:
                print("\nAll Books in Library:")
                for book_id, title in library.items():
                    print(f"{book_id} → {title}")
            else:
                print("Library is empty!")

        elif choice == 6:
            print("Total number of books:", len(library))

        elif choice == 7:
            title = input("Enter Book Title to search: ")
            if title in library.values():
                print("Yes, this book exists in the library!")
            else:
                print("Book not found!")

        elif choice == 8:
            print("Exiting Library System. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
library_system()
