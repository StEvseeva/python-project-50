from gendiff.engine import generate_diff, parse, run_gendiff
from gendiff.formaters import plain
import os
import pytest


@pytest.fixture
def flat_answer():
    return (parse(os.path.join('gendiff',
                              'tests',
                              'fixtures',
                              'flat_answer.json')))


@pytest.fixture
def deep_answer():
    return (parse(os.path.join('gendiff',
                               'tests',
                               'fixtures',
                               'deep_answer.json')))


@pytest.fixture
def flat_data1():
    return {"host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False}


@pytest.fixture
def flat_data2():
    return {"timeout": 20, "verbose": True, "host": "hexlet.io"}


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


def test_generate_giff_flat(flat_answer, flat_data1, flat_data2):

    assert generate_diff(flat_data1, flat_data2) == flat_answer
    assert generate_diff({}, {}) == {}


def test_generate_giff_deep(deep_answer):

    deep_data1 = parse(os.path.join('gendiff',
                                    'tests',
                                    'fixtures',
                                    'deep1.json'))
    deep_data2 = parse(os.path.join('gendiff',
                                    'tests',
                                    'fixtures',
                                    'deep2.json'))

    assert generate_diff(deep_data1, deep_data2) == deep_answer


# def test_rungendiff(capfd):
#     file1_path = os.path.join('gendiff',
#                               'tests',
#                               'fixtures',
#                               'deep1.json')
#     file2_path = os.path.join('gendiff',
#                               'tests',
#                               'fixtures',
#                               'deep2.json')
#     answer = open(os.path.join('gendiff',
#                           'tests',
#                           'fixtures',
#                           'deep_answer')).read()
#     run_gendiff(file1_path, file2_path, 'stylish')
#     out, err = capfd.readouterr()
#     assert out == answer


def test_plain_format(capfd, deep_answer):
    plain(deep_answer)
    out, err = capfd.readouterr()
    expected_out = open(os.path.join('gendiff',
                                 'tests',
                                 'fixtures',
                                 'plain_answer')).read()
    assert out == expected_out