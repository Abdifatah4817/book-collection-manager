# book-collection-manager
A comprehensive Command Line Interface (CLI) application for managing your personal book collection. Built with Python, SQLAlchemy ORM, and following object-oriented programming best practices.

## Features
- **Book Management**: Add, view, search, update, and delete books
- **Author Management**: Manage authors and view their books
- **Genre Management**: Organize books by genres
- **Advanced Search**: Find books by title, author, or genre
- **Statistics**: View collection statistics and reading insights
- **Data Validation**: Input validation and error handling

## Database Schema

The application uses SQLite database with three main tables:

- **Books**: Stores book information (title, ISBN, year, rating, pages)
- **Authors**: Stores author information (name, nationality)
- **Genres**: Stores genre information (name, description)

### Relationships:
- **One-to-Many**: Author → Books (one author can have many books)
- **One-to-Many**: Genre → Books (one genre can have many books)

## Installation
## ✅ Verified Features & Testing Results

### Database Operations:
- ✅ **CRUD Operations**: Full Create, Read, Update, Delete for all entities
- ✅ **Relationships Verified**: One-to-many relationships working correctly
- ✅ **Data Integrity**: Unique constraints and foreign keys enforced

### Calculated Properties:
- ✅ **Reading Time**: Automatically calculated based on page count
- ✅ **Book Age**: Calculated from publication year to current year
- ✅ **Statistics**: Collection totals, averages, and summaries

### User Experience:
- ✅ **Input Validation**: Year, rating, and pages validated
- ✅ **Error Handling**: Graceful error recovery and user feedback
- ✅ **Search Functionality**: Cross-table search by title, author, or genre

1. Clone the repository:
```bash
git clone <repository-url>
cd book_collection_manager