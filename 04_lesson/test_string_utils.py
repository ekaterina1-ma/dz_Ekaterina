import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  Skypro", "Skypro"),
    (" Hello", "Hello"),
    ("    Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123123", "123123"),
    ("", ""),
    ("mama", "mama"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "S", True),
    ("hello", "h", True),
    ("world", "w", True),
])
def test_contains_positive(input_str, char, expected):
    assert string_utils.contains(input_str, char) is expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "z", False),
    ("hello", "x", False),
    ("world", "q", False),
])
def test_contains_negative(input_str, char, expected):
    assert string_utils.contains(input_str, char) is expected


def test_contains_none():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")
    with pytest.raises(AttributeError):
        string_utils.contains("hello", None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, char, expected", [
    ("SkyPro", "S", "kyPro"),
    ("Hello", "H", "ello"),
    ("world", "w", "orld"),
])
def test_delete_symbol_positive(input_str, char, expected):
    assert string_utils.delete_symbol(input_str, char) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, char, expected", [
    ("mama", "z", "mama"),
    ("hello", "x", "hello"),
    ("by", " ", "by"),
])
def test_delete_symbol_negative(input_str, char, expected):
    assert string_utils.delete_symbol(input_str, char) == expected


def test_delete_symbol_raises():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
    with pytest.raises(AttributeError):
        string_utils.delete_symbol("hello", None)
