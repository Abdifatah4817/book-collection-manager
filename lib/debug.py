#!/usr/bin/env python3
"""
Debug script for Book Collection Manager.
Runs basic tests to make sure models, relationships, and queries work.
"""

from models import Author, Genre, Book, session
from database.setup import create_tables
from datetime import datetime


def debug():
    print("\nStarting debug script...")
    print("----------------------------------------")

    # 1. Setup database
    print("Creating tables...")
    create_tables()

    # 2. Clear existing data
    print("Resetting database...")
    session.query(Book).delete()
    session.query(Author).delete()
    session.query(Genre).delete()
    session.commit()

    # 3. Add sample authors
    print("Adding authors...")
    author1 = Author.create_author("J.K. Rowling", "British")
    author2 = Author.create_author("George Orwell", "British")
    author3 = Author.create_author("Stephen King", "American")
    author4 = Author.create_author("Agatha Christie", "British")

    # 4. Add sample genres
    print("Adding genres...")
    genre1 = Genre.create_genre("Fantasy", "Magical/supernatural")
    genre2 = Genre.create_genre("Science Fiction", "Futuristic themes")
    genre3 = Genre.create_genre("Mystery", "Detective stories")
    genre4 = Genre.create_genre("Horror", "Suspense and fear")

    # 5. Add sample books
    print("Adding books...")

    book1 = Book.create_book(
        "Harry Potter and the Philosopher's Stone",
        "978-0439708180", 1997, author1.id, genre1.id, 4.8, 320
    )

    book2 = Book.create_book(
        "1984",
        "978-0451524935", 1949, author2.id, genre2.id, 4.7, 328
    )

    book3 = Book.create_book(
        "Animal Farm",
        "978-0451526342", 1945, author2.id, genre2.id, 4.5, 112
    )

    book4 = Book.create_book(
        "The Shining",
        "978-0307743657", 1977, author3.id, genre4.id, 4.6, 447
    )

    book5 = Book.create_book(
        "Murder on the Orient Express",
        "978-0062693662", 1934, author4.id, genre3.id, 4.4, 274
    )

    print("Sample data inserted.")

    # --------------------------
    # Tests
    # --------------------------

    print("\nTesting author-book relationships...")
    for author in [author1, author2, author3, author4]:
        print(f"- {author.name}: {author.book_count} book(s)")
        for b in author.books:
            print(f"    {b.title}")

    print("\nTesting genre-book relationships...")
    for genre in [genre1, genre2, genre3, genre4]:
        print(f"- {genre.name}: {genre.book_count} book(s)")
        for b in genre.books:
            print(f"    {b.title} ({b.author.name})")

    print("\nTesting book details...")
    for b in [book1, book2, book3, book4, book5]:
        print(f"{b.title}:")
        print(f"  Reading time: {b.reading_time} hrs")
        print(f"  Age: {b.age} years")
        print(f"  Author: {b.author.name}")
        print(f"  Genre: {b.genre.name}")

    print("\nChecking database totals...")
    all_books = Book.get_all_books()
    all_authors = Author.get_all_authors()
    all_genres = Genre.get_all_genres()

    print(f"Books: {len(all_books)}")
    print(f"Authors: {len(all_authors)}")
    print(f"Genres: {len(all_genres)}")

    print("\nTesting search...")
    print("Search 'Harry':")
    for b in Book.find_by_title("Harry"):
        print(" ", b.title)

    print("Search author 'King':")
    for a in Author.find_by_name("King"):
        print(" ", a.name)
        print("   Books:", ", ".join([bk.title for bk in a.books]))

    print("\nChecking collection stats...")
    if all_books:
        total_pages = sum(b.pages for b in all_books)
        avg_rating = sum(b.rating for b in all_books) / len(all_books)
        total_hours = sum(b.reading_time for b in all_books)

        print("Total pages:", total_pages)
        print("Average rating:", round(avg_rating, 2))
        print("Total reading time:", total_hours)

    print("\nDone. Debug checks completed.")
    print("----------------------------------------")


if __name__ == "__main__":
    debug()
