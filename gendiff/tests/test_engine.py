from gendiff.engine import generate_diff, parse
import pytest


@pytest.fixture
def flat_answer():
    return (open('gendiff/tests/fixtures/flat_answer')).read()


@pytest.fixture
def deep_answer():
    return (open('gendiff/tests/fixtures/deep_answer')).read()


@pytest.fixture
def flat_data1():
    return {"host": "hexlet.io", "timeout": 50,
         "proxy": "123.234.53.22", "follow": False}


@pytest.fixture
def flat_data2():
    return {"timeout": 20, "verbose": True, "host": "hexlet.io"}


@pytest.fixture
def deep_data1():
    return


@pytest.fixture
def deep_data2():
    return


def test_generate_giff_flat(flat_answer, flat_data1, flat_data2):

    assert generate_diff(flat_data1, flat_data2) == flat_answer
    assert generate_diff({}, {}) == '{}'


def test_generate_giff_deep(deep_answer, deep_data1, deep_data2):

    assert generate_diff(deep_data1, deep_data2) == deep_answer


def test_parser(flat_data1, flat_data2):

    path_to_json1 = 'gendiff/tests/fixtures/file1.json'
    path_to_yaml1 = 'gendiff/tests/fixtures/file1.yaml'
    path_to_yaml2 = 'gendiff/tests/fixtures/file2.yml'
    path_to_deep_yaml = 'gendiff/tests/fixtures/deep2.yaml'
    path_to_deep_json = 'gendiff/tests/fixtures/deep2.json'

    assert parse(path_to_json1) == flat_data1
    assert parse(path_to_yaml1) == flat_data1
    assert parse(path_to_yaml2) == flat_data2
    assert parse(path_to_deep_yaml) == parse(path_to_deep_json)


