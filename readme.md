# Movie Rating System

## About

This project is a Python-based movie rating system that processes and analyzes movie data. It provides functionality to:

- **Refactor Data**: Convert raw movie data from list format to structured dictionaries
- **Sort Movies**: Filter and sort movies based on ratings and certification status
- **Get Top Rated Movies**: Retrieve the top 10 highest-rated "certified fresh" movies

The system uses a modular architecture with separate classes for data refactoring (`RefactorData`) and movie sorting (`SortMovies`). The movie data includes:
- Movie ID
- Rating (0.0 - 9.0 scale)
- Title
- Certified Fresh status (boolean)

## How to Run

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Running the Application

1. **Clone or navigate to the project directory:**
   ```bash
   cd /path/to/project
   ```

2. **Run the main application:**
   ```bash
   python main.py
   ```

The application will:
- Load the movie data from `data.py`
- Process the data using the `RefactorData` and `SortMovies` classes
- Display the top 10 highest-rated certified fresh movies

### Project Structure

```
softwaremind/
├── main.py              # Main application entry point
├── data.py              # Movie data source
├── src/
│   └── movies/
│       ├── __init__.py
│       ├── refactor_data.py    # Data conversion logic
│       └── sort_movies.py      # Movie sorting and filtering
└── tests/
    ├── __init__.py
    ├── mocks.py                # Test data and mocks
    ├── test_refactor_data.py   # Tests for RefactorData class
    └── test_sort_movies.py     # Tests for SortMovies class
```

## How to Test

### Running Tests

The project includes a comprehensive test suite using Python's `unittest` framework.

1. **Run all tests:**
   ```bash
   python -m unittest discover tests
   ```

2. **Run specific test files:**
   ```bash
   # Test the RefactorData class
   python -m unittest tests.test_refactor_data
   
   # Test the SortMovies class
   python -m unittest tests.test_sort_movies
   ```

3. **Run tests with verbose output:**
   ```bash
   python -m unittest discover tests -v
   ```

### Test Data

The tests use mock data defined in `tests/mocks.py` to ensure consistent and isolated testing without depending on the actual movie data in `data.py`.

### Expected Test Output

When tests pass successfully, you should see output similar to:
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

If any tests fail, the output will show detailed information about which tests failed and why.
