mock_movie_list = [
    [1, 9.0, 'Interstellar', True],
    [2, 8.5, 'Fast and the Furious', True],
    [3, 7.0, 'The Dark Knight', False],
    [4, 6.5, 'The Dark Knight Rises', False],
    [5, 6.0, 'The Dark Knight', False],
    [6, 5.5, 'The Dark Knight Rises', False],
    [7, 5.0, 'The Dark Knight', False],
    [8, 4.5, 'The Dark Knight Rises', False],
    [9, 6, 'Test', True],
    [10, 8, 'Test 2', True],
]

refactored_movie_list = [
    {
        'id': 1,
        'rating': 9.0,
        'title': 'Interstellar',
        'certified_fresh': True,
    },
    {
        'id': 2,
        'rating': 8.5,
        'title': 'Fast and the Furious',
        'certified_fresh': True,
    },
    {
        'id': 3,
        'rating': 7.0,
        'title': 'The Dark Knight',
        'certified_fresh': False,
    },
    {
        'id': 4,
        'rating': 6.5,
        'title': 'The Dark Knight Rises',
        'certified_fresh': False,
    },
    {
        'id': 5,
        'rating': 6.0,
        'title': 'The Dark Knight',
        'certified_fresh': False,
    },
    {
        'id': 6,
        'rating': 5.5,
        'title': 'The Dark Knight Rises',
        'certified_fresh': False,
    },
    {
        'id': 7,
        'rating': 5.0,
        'title': 'The Dark Knight',
        'certified_fresh': False,
    },
    {
        'id': 8,
        'rating': 4.5,
        'title': 'The Dark Knight Rises',
        'certified_fresh': False,
    },
    {
        'id': 9,
        'rating': 6,
        'title': 'Test',
        'certified_fresh': True,
    },
    {
        'id': 10,
        'rating': 8,
        'title': 'Test 2',
        'certified_fresh': True,
    },
]

certified_fresh_movie_list = [
    {
        'id': 1,
        'rating': 9.0,
        'title': 'Interstellar',
        'certified_fresh': True,
    },
    {
        'id': 2,
        'rating': 8.5,
        'title': 'Fast and the Furious',
        'certified_fresh': True,
    },
    {
        'id': 9,
        'rating': 6,
        'title': 'Test',
        'certified_fresh': True,
    },
    {
        'id': 10,
        'rating': 8,
        'title': 'Test 2',
        'certified_fresh': True,
    },
]

top_rated_movie_list = [
    {
        'id': 1,
        'rating': 9.0,
        'title': 'Interstellar',
        'certified_fresh': True,
    },
    {
        'id': 2,
        'rating': 8.5,
        'title': 'Fast and the Furious',
        'certified_fresh': True,
    },
    {
        'id': 10,
        'rating': 8,
        'title': 'Test 2',
        'certified_fresh': True,
    },
    {
        'id': 9,
        'rating': 6,
        'title': 'Test',
        'certified_fresh': True,
    },
]
