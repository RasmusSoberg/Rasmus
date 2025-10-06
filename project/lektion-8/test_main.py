from main import add
import pytest

def test_addition():
    assert add(2, 2) == 4

def test_sum_list():
    numbers = [1, 2, 3]
    assert sum(numbers) == 6

def test_max_list():
    numbers = [1, 2, 3]
    assert max(numbers) == 3

@pytest.fixture
def numbers():
    return [1, 2, 3]

def test_sum(numbers):
    assert sum(numbers) == 6

def test_max(numbers):
    assert max(numbers) == 3

@pytest.fixture
def temporary_file(tmp_path):
    file_path = tmp_path / 'data.txt'
    with open (file_path, 'w') as f:
        f.write('hello world')
    yield file_path
    file_path.unlink() 

def test_ifle_contents(temporary_file):
    with open(temporary_file) as f:
        content = f.read()
        assert content == 'hello world'
