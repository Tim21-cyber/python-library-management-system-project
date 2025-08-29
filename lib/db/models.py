from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)

class Patron(Base):
    __tablename__ = 'patrons'
    id = Column(Integer, primary_key=True)
    _name = Column("name", String)
    books = relationship("Book", back_populates="patron")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @classmethod
    def create(cls, name):
        session = Session()
        try:
            patron = cls()
            patron.name = name
            session.add(patron)
            session.commit()
            patron_id = patron.id  # Store ID before session close
            session.close()
            return patron_id  # Return ID instead of object
        except ValueError as e:
            session.rollback()
            raise e
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def delete(cls, id):
        session = Session()
        patron = session.query(cls).get(id)
        if patron:
            session.delete(patron)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def get_all(cls):
        session = Session()
        patrons = session.query(cls).all()
        session.close()
        return patrons

    @classmethod
    def find_by_id(cls, id):
        session = Session()
        patron = session.query(cls).get(id)
        session.close()
        return patron

    @classmethod
    def find_by_name(cls, name):
        session = Session()
        patron = session.query(cls).filter_by(_name=name).first()
        session.close()
        return patron

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    _title = Column("title", String)
    _author = Column("author", String)
    patron_id = Column(Integer, ForeignKey('patrons.id'))
    patron = relationship("Patron", back_populates="books")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Author must be a non-empty string")
        self._author = value

    @classmethod
    def create(cls, title, author, patron_id=None):
        session = Session()
        try:
            book = cls(patron_id=patron_id)
            book.title = title
            book.author = author
            session.add(book)
            session.commit()
            book_id = book.id  # Store ID before session close
            session.close()
            return book_id  # Return ID instead of object
        except ValueError as e:
            session.rollback()
            raise e
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    @classmethod
    def delete(cls, id):
        session = Session()
        book = session.query(cls).get(id)
        if book:
            session.delete(book)
            session.commit()
            session.close()
            return True
        session.close()
        return False

    @classmethod
    def get_all(cls):
        session = Session()
        books = session.query(cls).all()
        session.close()
        return books

    @classmethod
    def find_by_id(cls, id):
        session = Session()
        book = session.query(cls).get(id)
        session.close()
        return book

    @classmethod
    def find_by_title(cls, title):
        session = Session()
        book = session.query(cls).filter_by(_title=title).first()
        session.close()
        return book