#!/usr/bin/env python3

from models import Author, Genre, Book
from database.setup import create_tables
from models import session  # Add this import

def debug():
    """Debug function to test the models and relationships"""
    create_tables()
    
    # Clear existing data first to avoid UNIQUE constraint errors
    session.query(Genre).delete()
    session.query(Author).delete()
    session.query(Book).delete()
    session.commit()
    print("Cleared existing data")
    
    # Create authors
    author1 = Author.create_author("J.K. Rowling", "British")
    author2 = Author.create_author("George Orwell", "British")
    
    # Create genres
    genre1 = Genre.create_genre("Fantasy", "Magical and supernatural elements")
    genre2 = Genre.create_genre("Science Fiction", "Futuristic and scientific themes")
    
    # Create books
    book1 = Book.create_book("Harry Potter and the Philosopher's Stone", 
                            "978-0439708180", 1997, author1.id, genre1.id, 4.8, 320)
    
    book2 = Book.create_book("1984", "978-0451524935", 1949, author2.id, genre2.id, 4.7, 328)
    
    # Test relationships
    print(f"\nAuthor '{author1.name}' has {author1.book_count} books:")
    for book in author1.books:
        print(f"  - {book.title}")
    
    print(f"\nGenre '{genre1.name}' has {genre1.book_count} books:")
    for book in genre1.books:
        print(f"  - {book.title}")
    
    print(f"\nBook '{book1.title}' reading time: {book1.reading_time}")
    print(f"Book '{book2.title}' reading time: {book2.reading_time}")
    
    # Test queries
    print(f"\nAll books: {len(Book.get_all_books())}")
    print(f"All authors: {len(Author.get_all_authors())}")
    print(f"All genres: {len(Genre.get_all_genres())}")

if __name__ == "__main__":
    debug()