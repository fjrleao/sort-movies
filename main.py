from src.movies.refactor_data import RefactorData
from src.movies.sort_movies import SortMovies
from data import movie_list


def main():

    sort_movies = SortMovies(movie_list, RefactorData)
    print(sort_movies.get_top_rated_movie())


if __name__ == '__main__':
    main()
