from sqlalchemy.orm import sessionmaker
from lib.db.models import engine, Patron, Book


Session = sessionmaker(bind=engine)

def seed_database():
    session = Session()
    try:
        # Seed patrons
        patron1_id = Patron.create("Alice Smith")
        patron2_id = Patron.create("Bob Johnson")
        patron3_id = Patron.create("Carol White")
        
        # Seed books
        Book.create("The Great Gatsby", "F. Scott Fitzgerald", patron1_id)
        Book.create("1984", "George Orwell", patron1_id)
        Book.create("To Kill a Mockingbird", "Harper Lee", patron2_id)
        Book.create("Pride and Prejudice", "Jane Austen")
        
        session.commit()
        print("Database seeded successfully")
    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()
    