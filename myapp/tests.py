from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(title='Martin Eden', author='Jack London')

        self.assertEqual(str(book), 'Martin Eden')