from typing import List, Dict, Any
from abc import ABC, abstractmethod


class RefactorData:
    def __init__(self, movie_list: List[List[Any]]):
        self.movie_list = movie_list

    def convert_to_dict(self) -> List[Dict[str, Any]]:
        new_movie_list: List[Dict[str, Any]] = []
        for movie in self.movie_list:
            new_movie_list.append({
                'id': movie[0],
                'rating': movie[1],
                'title': movie[2],
                'certified_fresh': movie[3],
            })
        return new_movie_list
