

import unittest, os, sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src/lotr_sdk')))
from books import getBookById , getAllBooks , getBookByName, getBookChaptersById, getBookChapters, getBooksByRegex, Book


class TestBook(unittest.TestCase):

    def test_get_all_books(self):
        test_books = getAllBooks()
        self.assertEqual(len(test_books), 3)

    def test_book_by_id(self):
        test_book = getBookById("5cf5805fb53e011a64671582")
        self.assertEqual(test_book.id, "5cf5805fb53e011a64671582")
        self.assertNotEqual(test_book.id, "5cf5805fb53e011a64671581")
        self.assertEqual(test_book.name, "The Fellowship Of The Ring")
    
    def test_book_by_name(self):
        test_book = getBookByName("The Fellowship Of The Ring")
        self.assertEqual(test_book.id, "5cf5805fb53e011a64671582")
        self.assertNotEqual(test_book.id, "5cf5805fb53e011a64671581")
        self.assertEqual(test_book.name, "The Fellowship Of The Ring")

    def test_book_chapters_by_id(self):
        chapters = getBookChaptersById("5cf5805fb53e011a64671582")
        self.assertEqual(chapters.get("total"), 22)

    def test_book_chapters(self):
        book = Book("5cf5805fb53e011a64671582","The Fellowship Of The Ring")
        res = getBookChapters(book)
        self.assertEqual(res["total"], 22)
    
    def test_book_by_regex(self):
        books = getBooksByRegex("name", "/of/i")
        self.assertEqual(len(books), 2)
        self.assertIn("of", books[0].name.lower())


if __name__ == '__main__':
    unittest.main()
