from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from . import Base  

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    nationality = Column(String)
    biography = Column(Text)  # Added this field
    
    # One-to-many relationship with books
    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}', nationality='{self.nationality}')>"
    
    @classmethod
    def create_author(cls, name, nationality="", biography=""):
        """Create a new author if not exists"""
        from . import session
        
        # Check if author already exists (case-insensitive)
        existing = session.query(cls).filter(cls.name.ilike(name)).first()
        if existing:
            return existing  # Return existing author instead of creating new
        
        author = cls(name=name, nationality=nationality, biography=biography)
        session.add(author)
        session.commit()
        return author
    
    @classmethod
    def get_all_authors(cls):
        """Get all authors"""
        from . import session
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, author_id):
        """Find author by ID"""
        from . import session
        return session.query(cls).filter(cls.id == author_id).first()
    
    @classmethod
    def find_by_name(cls, name):
        """Find author by name (partial match, case-insensitive)"""
        from . import session
        return session.query(cls).filter(cls.name.ilike(f"%{name}%")).all()
    
    @classmethod
    def delete_author(cls, author_id):
        """Delete author by ID"""
        from . import session
        author = cls.find_by_id(author_id)
        if author:
            session.delete(author)
            session.commit()
            return True
        return False
    
    @property
    def book_count(self):
        """Return number of books by this author"""
        return len(self.books)
    
    def get_books(self):
        """Get all books by this author"""
        return self.books
    
    @property
    def book_titles(self):
        """Return list of book titles by this author"""
        return [book.title for book in self.books]