# Django REST API for Book Management

This project is a simple Django application that provides a RESTful API for managing books. It allows users to create, update, delete, and view books in a database.

## Features
- View a list of all books.
- View details of a single book.
- Add new books.
- Update existing books.
- Delete books.

## Technologies Used
- Python 3.11
- Django
- Django REST Framework
- SQLite (default database)

## Setup and Installation

### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.11+
- `pip`

### Installation
1. Clone the repository:
    git clone https://github.com/anageguchadze/CI-CD-Test.git

2. Create a virtual environment and activate it:
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt
    

4. Apply database migrations:
    python manage.py migrate
  

5. Create a superuser to access the Django admin (optional):
    python manage.py createsuperuser
    

6. Start the development server:
    python manage.py runserver
   

The application will be available at `http://127.0.0.1:8000/`.

### API Endpoints
- `GET /books/` - List all books.
- `POST /books/` - Create a new book.
- `GET /books/{id}/` - Get details of a specific book.
- `PUT /books/{id}/` - Update a specific book.
- `DELETE /books/{id}/` - Delete a specific book.

## Running Tests

To run the tests for the application:

python manage.py test


### Instructions:
1. Replace the URL in the **Installation** section with the actual URL of your GitHub repository.
2. If you're using a different database (e.g., PostgreSQL, MySQL), update the **Setup and Installation** section with the appropriate instructions for setting up the database.

This `README.md` provides a solid foundation for new developers who want to contribute or run the project on their own machine.
