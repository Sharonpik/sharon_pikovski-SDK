import unittest, os, sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src/lotr_sdk')))
from movies import Movie, getAllMovies, getAllMoviesSorted, getMovieById, getMovieByName, getMoviesByComparison, getMoviesByRegex

class TestBook(unittest.TestCase):

    def test_create_move_empty(self):
        test_movie = Movie()
        self.assertEqual(test_movie.id,"")
        self.assertEqual(test_movie.name,"")
        self.assertEqual(test_movie.run_time_minutes,0)
        self.assertEqual(test_movie.budget_millions,0)
        self.assertEqual(test_movie.box_office_revenue_millions,0)
        self.assertEqual(test_movie.academy_award_nominations,0)
        self.assertEqual(test_movie.academy_award_wins,0)
        self.assertEqual(test_movie.rotten_tomatoes_score,0)

    def test_get_all_movies(self):
        test_movies = getAllMovies()
        self.assertEqual(len(test_movies),8)


    def test_get_sorted_movies(self):
        test_movies = getAllMoviesSorted("name","asc")
        self.assertEqual(test_movies[0].name,"The Battle of the Five Armies")
        self.assertEqual(test_movies[7].name,"The Unexpected Journey")

    def test_get_movie_by_id(self):
        test_movie = getMovieById("5cd95395de30eff6ebccde58")
        self.assertEqual(test_movie.name,"The Unexpected Journey")
        self.assertEqual(test_movie.id,"5cd95395de30eff6ebccde58")

    def test_get_movie_by_name(self):
        test_movie = getMovieByName("The Unexpected Journey")
        self.assertEqual(test_movie.name,"The Unexpected Journey")
        self.assertEqual(test_movie.id,"5cd95395de30eff6ebccde58")

    def test_get_movie_by_comparison(self):
        test_movies = getMoviesByComparison("budgetInMillions", "<", "100")
        self.assertEqual(len(test_movies),3)
    
    def test_get_movie_by_regex(self):
        test_movies = getMoviesByRegex("name","/Return/i")
        self.assertIn("Return",test_movies[0].name)


if __name__ == '__main__':
    unittest.main()
