import unittest
from src.movies.refactor_data import RefactorData
from tests.mocks import mock_movie_list, refactored_movie_list


class TestRefactorData(unittest.TestCase):
    def setUp(self):
        self.refactor_data = RefactorData(mock_movie_list)

    def test_convert_to_dict(self):
        refactored_movie_list = self.refactor_data.convert_to_dict()
        assert refactored_movie_list == refactored_movie_list
