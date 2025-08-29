import sys
from lib.db.models import Base, engine, Patron, Book

Base.metadata.create_all(engine)

def display_patron(p):
    if p:
        print(f"ID: {p.id}, Name: {p.name}")
    else:
        print("Not found")

def display_book(b):
    if b:
        print(f"ID: {b.id}, Title: {b.title}, Author: {b.author}, Borrowed by: {b.patron.name if b.patron else 'None'}")
    else:
        print("Not found")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Manage Patrons")
        print("2. Manage Books")
        print("3. Exit")
        choice = input("Choose: ").strip()
        if choice == '1':
            manage_patrons()
        elif choice == '2':
            manage_books()
        elif choice == '3':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice")

def manage_patrons():
    while True:
        print("\nPatrons Menu:")
        print("1. Create Patron")
        print("2. Delete Patron")
        print("3. Display All Patrons")
        print("4. Find Patron by ID")
        print("5. Find Patron by Name")
        print("6. View Borrowed Books")
        print("7. Back")
        choice = input("Choose: ").strip()
        if choice == '1':
            name = input("Name: ").strip()
            try:
                patron = Patron.create(name)
                print(f"Created Patron ID: {patron.id}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        elif choice == '2':
            try:
                id = int(input("ID: ").strip())
                if Patron.delete(id):
                    print("Deleted")
                else:
                    print("Not found")
            except ValueError:
                print("Invalid ID")
        elif choice == '3':
            patrons = Patron.get_all()
            if not patrons:
                print("No patrons")
            for p in patrons:
                print(f"ID: {p.id}, Name: {p.name}")
        elif choice == '4':
            try:
                id = int(input("ID: ").strip())
                p = Patron.find_by_id(id)
                display_patron(p)
            except ValueError:
                print("Invalid ID")
        elif choice == '5':
            name = input("Name: ").strip()
            p = Patron.find_by_name(name)
            display_patron(p)
        elif choice == '6':
            try:
                id = int(input("Patron ID: ").strip())
                p = Patron.find_by_id(id)
                if p:
                    print("Borrowed books:")
                    if not p.books:
                        print("None")
                    for b in p.books:
                        print(f"ID: {b.id}, Title: {b.title}, Author: {b.author}")
                else:
                    print("Not found")
            except ValueError:
                print("Invalid ID")
        elif choice == '7':
            return
        else:
            print("Invalid choice")

def manage_books():
    while True:
        print("\nBooks Menu:")
        print("1. Create Book")
        print("2. Delete Book")
        print("3. Display All Books")
        print("4. Find Book by ID")
        print("5. Find Book by Title")
        print("6. View Borrowing Patron")
        print("7. Back")
        choice = input("Choose: ").strip()
        if choice == '1':
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            patron_id_input = input("Patron ID (optional): ").strip()
            patron_id = int(patron_id_input) if patron_id_input else None
            if patron_id:
                if not Patron.find_by_id(patron_id):
                    print("Patron not found")
                    continue
            try:
                book = Book.create(title, author, patron_id)
                print(f"Created Book ID: {book.id}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        elif choice == '2':
            try:
                id = int(input("ID: ").strip())
                if Book.delete(id):
                    print("Deleted")
                else:
                    print("Not found")
            except ValueError:
                print("Invalid ID")
        elif choice == '3':
            books = Book.get_all()
            if not books:
                print("No books")
            for b in books:
                patron_name = b.patron.name if b.patron else 'None'
                print(f"ID: {b.id}, Title: {b.title}, Author: {b.author}, Borrowed by: {patron_name}")
        elif choice == '4':
            try:
                id = int(input("ID: ").strip())
                b = Book.find_by_id(id)
                display_book(b)
            except ValueError:
                print("Invalid ID")
        elif choice == '5':
            title = input("Title: ").strip()
            b = Book.find_by_title(title)
            display_book(b)
        elif choice == '6':
            try:
                id = int(input("Book ID: ").strip())
                b = Book.find_by_id(id)
                if b:
                    if b.patron:
                        display_patron(b.patron)
                    else:
                        print("Not borrowed")
                else:
                    print("Not found")
            except ValueError:
                print("Invalid ID")
        elif choice == '7':
            return
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()