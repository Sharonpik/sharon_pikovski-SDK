import unittest, os, sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src/lotr_sdk')))
from characters import Character, getAllCharacters ,getCharacterByName , getCharacterById, getCharacterQuotesById, getCharacterQuotesByName,getCharacterQuotes
from characters import getAllCharacterWithoutSome, getAllCharactersByOption ,getSortedCharacters, getCharacterByRegex

class TestBook(unittest.TestCase):

    def test_create_chapter_empty(self):
        test_character = Character()
        self.assertEqual(test_character.id,"")
        self.assertEqual(test_character.height,"")
        self.assertEqual(test_character.race,"")
        self.assertEqual(test_character.gender,"")
        self.assertEqual(test_character.birth,"")
        self.assertEqual(test_character.spouse,"")
        self.assertEqual(test_character.death,"")
        self.assertEqual(test_character.realm,"")
        self.assertEqual(test_character.hair,"")
        self.assertEqual(test_character.name,"")
        self.assertEqual(test_character.wikiUrl,"")

    def test_all_characters(self):
        test_characters = getAllCharacters()
        self.assertEqual(len(test_characters),933)

    def test_character_by_name(self):
        test_character = getCharacterByName("Gandalf")
        self.assertEqual(test_character.name,"Gandalf")
        self.assertEqual(test_character.id,"5cd99d4bde30eff6ebccfea0")

    def test_character_by_id(self):
        test_character = getCharacterById("5cd99d4bde30eff6ebccfea0")
        self.assertEqual(test_character.name,"Gandalf")
        self.assertEqual(test_character.id,"5cd99d4bde30eff6ebccfea0")

    def test_character_quotes_by_id(self):
        test_quotes = getCharacterQuotesById("5cd99d4bde30eff6ebccfea0")
        self.assertEqual(len(test_quotes),216)

    def test_character_quotes_by_name(self):
        test_quotes = getCharacterQuotesByName("Gandalf")
        self.assertEqual(len(test_quotes),216)

    def test_character_quotes(self):
        test_character = getCharacterByName("Gandalf")
        test_quotes = getCharacterQuotes(test_character)
        self.assertEqual(len(test_quotes),216)

    def test_all_characters_without_some(self):
        test_characters = getAllCharacterWithoutSome(["Gandalf","Bilbo"])
        self.assertEqual(len(test_characters),932)

    def test_all_characters_by_option(self):
        test_characters = getAllCharactersByOption("race", "Human")
        self.assertEqual(len(test_characters),388)
        self.assertEqual(test_characters[0].race,"Human")

    def test_get_sorted_characters(self):
        test_characters = getSortedCharacters("name", "asc")
        self.assertEqual(test_characters[0].name,"Adaldrida (Bolger) Brandybuck")
        self.assertEqual(test_characters[932].name,"Óin (King of Durin's Folk)")

    def test_get_characters_by_regex(self):
        test_characters = getCharacterByRegex("name", "/foot/i")
        self.assertIn("foot",test_characters[0].name)
        


if __name__ == '__main__':
    unittest.main()
