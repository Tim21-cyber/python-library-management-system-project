from db.models import Session, Patron, Book

def debug_database():
    session = Session()
    try:
        print("\nAll Patrons:")
        patrons = Patron.get_all()
        for patron in patrons:
            print(f"ID: {patron.id}, Name: {patron.name}")
            print("Borrowed Books:")
            for book in patron.books:
                print(f"  - ID: {book.id}, Title: {book.title}, Author: {book.author}")
            print()

        print("All Books:")
        books = Book.get_all()
        for book in books:
            patron_name = book.patron.name if book.patron else "None"
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Borrowed by: {patron_name}")
    except Exception as e:
            print(f"Error debugging database: {e}")
    finally:
        session.close()

if __name__ == "__main__":
        debug_database()