from gendiff.engine import generate_diff


def test_generate_giff():

    a = {"host": "hexlet.io", "timeout": 50,
         "proxy": "123.234.53.22", "follow": False}
    b = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
    answer = (open('gendiff/tests/fixtures/answer1')).read()
    assert generate_diff(a, b) == answer
