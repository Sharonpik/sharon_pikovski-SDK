
import unittest, os, sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src/lotr_sdk')))
from quotes import Quote, getAllLotrQuoates, getQuoteById, getQuotesSorted, getQuotesByRegex

class TestBook(unittest.TestCase):

    def test_create_quote_empty(self):
        test_quote = Quote()

        self.assertEqual(test_quote.id, "")
        self.assertEqual(test_quote.dialog, "")
        self.assertEqual(test_quote.movie, "")
        self.assertEqual(test_quote.character, "")


    def test_get_all_quotes(self):
        test_quote = getAllLotrQuoates()
        self.assertEqual(len(test_quote),2390)

    def test_get_sorted_quotes(self):
        test_quotes = getQuotesSorted("dialog", "asc")
        self.assertEqual(test_quotes[0].dialog, "")
        self.assertEqual(test_quotes[0].id, "5cd96e05de30eff6ebccebdb")

    def test_get_movie_by_id(self):
        test_quote = getQuoteById("5cd96e05de30eff6ebcce7f0")
        self.assertEqual(test_quote.dialog,"They cursed us")
        self.assertEqual(test_quote.id,"5cd96e05de30eff6ebcce7f0")

    def test_get_movie_by_id(self):
        test_quotes = getQuotesByRegex("dialog", "/cursed/i")
        self.assertIn("cursed",test_quotes[0].dialog)


if __name__ == '__main__':
    unittest.main()
