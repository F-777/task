import unittest
from app.models import Bo

class TestBook(unittest.TestCase):
    def test_check_out(self):
        book = Book('Tet Book', 'Author', 2020)
        book.check_out()
        self.assertTrue(book.is_checked_out)
    
    def test_check_in(self):
        book = Book('Tet Book', 'Author', 2020)
        book.check_out()
        book.check_in()
        self.assertFalse(book.is_checked_out)

if __name__ == '__main__':
