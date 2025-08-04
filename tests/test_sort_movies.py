import unittest
from unittest.mock import Mock, patch
from src.movies.sort_movies import SortMovies
from tests.mocks import mock_movie_list, refactored_movie_list, top_rated_movie_list


class TestSortMovies(unittest.TestCase):

    def setUp(self):
        self.mock_refactor_data_instance = Mock()
        self.mock_refactor_data_instance.convert_to_dict.return_value = refactored_movie_list

        self.mock_refactor_data_class = Mock()
        self.mock_refactor_data_class.return_value = self.mock_refactor_data_instance
        self.sort_movies = SortMovies(
            mock_movie_list, self.mock_refactor_data_class
        )

    def test_get_certified_fresh_movies(self):
        certified_fresh_movies = self.sort_movies.get_certified_fresh_movies()

        self.mock_refactor_data_class.assert_called_once_with(mock_movie_list)
        self.mock_refactor_data_instance.convert_to_dict.assert_called_once()
        assert all(
            movie['certified_fresh']
            for movie in certified_fresh_movies
        )
        assert len(certified_fresh_movies) == 4

    def test_get_top_rated_movie(self):
        top_rated_movies = self.sort_movies.get_top_rated_movie()
        expected_top_rated = top_rated_movie_list
        assert top_rated_movies == expected_top_rated
