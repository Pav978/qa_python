import pytest
from main import BooksCollector

#фикстура
@pytest.fixture
def collector():
    return BooksCollector()