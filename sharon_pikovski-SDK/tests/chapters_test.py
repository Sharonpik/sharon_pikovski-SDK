import unittest, os, sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src/lotr_sdk')))
from chapters import Chapter, getAllChapters, getChapterById, getChapterByName, getSortedChapters, getChapterByRegex

class TestBook(unittest.TestCase):

    def test_create_chapter_empty(self):
        test_chapter = Chapter()
        self.assertEqual(test_chapter.id, "")
        self.assertEqual(test_chapter.chapterName, "")
        self.assertEqual(test_chapter.book, "")

    def test_get_all_chapters(self):
        test_chapters = getAllChapters()
        self.assertEqual(len(test_chapters), 62)
        self.assertNotEqual(test_chapters[0].id, "")
        self.assertNotEqual(test_chapters[0].chapterName, "")
        self.assertNotEqual(test_chapters[0].book, "")

    def test_get_chapter_by_id(self):
        test_chapter = getChapterById("6091b6d6d58360f988133b8b")
        self.assertEqual(test_chapter.id, "6091b6d6d58360f988133b8b")
        self.assertEqual(test_chapter.chapterName, "A Long-expected Party")
        self.assertEqual(test_chapter.book, "5cf5805fb53e011a64671582")  

    def test_get_chapter_by_name(self):
        test_chapter = getChapterByName("A Long-expected Party")
        self.assertEqual(test_chapter.id, "6091b6d6d58360f988133b8b")
        self.assertEqual(test_chapter.chapterName, "A Long-expected Party")
        self.assertEqual(test_chapter.book, "5cf5805fb53e011a64671582") 

    def test_get_asc_sorted_chapters(self):
        test_chapters = getSortedChapters("chapterName", "asc")
        self.assertEqual(test_chapters[0].id, "6091b6d6d58360f988133b8f")
        self.assertEqual(test_chapters[0].chapterName, "A Conspiracy Unmasked")
        self.assertEqual(test_chapters[0].book, "5cf5805fb53e011a64671582")  

    def test_get_desc_sorted_chapters(self):
        test_chapters = getSortedChapters("chapterName", "desc")
        self.assertEqual(test_chapters[0].id, "6091b6d6d58360f988133ba4")
        self.assertEqual(test_chapters[0].chapterName, "Treebeard")
        self.assertEqual(test_chapters[0].book, "5cf58077b53e011a64671583")           
         
    def test_get_chapters(self):
        test_chapters = getChapterByRegex("chapterName", "/Knife/i")
        self.assertIn("Knife",test_chapters[0].chapterName) 


if __name__ == '__main__':
    unittest.main()
