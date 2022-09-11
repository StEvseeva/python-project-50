from gendiff.engine import generate_diff, parse
import pytest


@pytest.fixture
def answer():
    return (open('gendiff/tests/fixtures/answer1')).read()


@pytest.fixture
def data1():
    return {"host": "hexlet.io", "timeout": 50,
         "proxy": "123.234.53.22", "follow": False}


@pytest.fixture
def data2():
    return {"timeout": 20, "verbose": True, "host": "hexlet.io"}


def test_generate_giff(answer, data1, data2):

    assert generate_diff(data1, data2) == answer
    assert generate_diff({}, {}) == '{}'


def test_parser(data1, data2):

    path_to_json1 = 'gendiff/tests/fixtures/file1.json'
    path_to_yaml1 = 'gendiff/tests/fixtures/file1.yaml'
    path_to_yaml2 = 'gendiff/tests/fixtures/file2.yml'

    assert parse(path_to_json1) == data1
    assert parse(path_to_yaml1) == data1
    assert parse(path_to_yaml2) == data2
