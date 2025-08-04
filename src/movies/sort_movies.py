from typing import List, Dict, Any
from src.movies.refactor_data import RefactorData


class SortMovies:
    def __init__(self, movie_list: List[List[Any]], refactor_data: RefactorData):
        self.movie_list = movie_list
        self.refactor_data = refactor_data(self.movie_list)

    def get_certified_fresh_movies(self) -> List[Dict[str, Any]]:
        movies = self.refactor_data.convert_to_dict()
        return [movie for movie in movies if movie['certified_fresh']]

    def get_top_rated_movie(self) -> List[Dict[str, Any]]:
        return sorted(self.get_certified_fresh_movies(), key=lambda x: x['rating'], reverse=True)[:10]
