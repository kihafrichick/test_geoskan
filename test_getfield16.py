import pytest
from getfield16 import getfield16


@pytest.mark.parametrize("hex_str, start_bit, expected", [
    ('0123456789ABCDEF', 0, '0123'),
    ('0123456789ABCDEF', 32, '89AB'),
    ('0123456789ABCDEF', 7, '91A2'),
    ('0000', 0, '0000'),
    ('FFFF', 0, 'FFFF'),
    ('F' * 32, 0, 'FFFF'),
    ('F' * 32, 112, 'FFFF'),
    ('0123456789ABCDEF', 16, '4567'),
    ('0123456789ABCDEF', 48, 'CDEF'),
    ('0123456789abcdef', 0, '0123'),
    ('abcdef', 0, 'ABCD'),
], ids=[
    "example_1_start_0",
    "example_2_start_32",
    "example_3_start_7",
    "min_length_all_zeros",
    "min_length_all_F",
    "max_length_start_0",
    "max_length_start_112",
    "start_16",
    "start_48",
    "lowercase_hex",
    "lowercase_abcdef",
])
def test_valid_cases(hex_str, start_bit, expected):
    assert getfield16(hex_str, start_bit) == expected


@pytest.mark.parametrize("hex_str, start_bit, expected_error", [
    ('0123456789ABCDEF', 62, 'Ошибка: некорректный стартовый бит'),
    ('0123456789ABCDEF', 49, 'Ошибка: некорректный стартовый бит'),
    ('0123456789ABCDEF', -1, 'Ошибка: некорректный стартовый бит'),
    ('0000', 1, 'Ошибка: некорректный стартовый бит'),
    ('F' * 32, 113, 'Ошибка: некорректный стартовый бит'),
    ('wrong_hex_string', 0, 'Ошибка: недопустимые символы в hex-строке'),
    ('0123456789ABCDEF!', 0, 'Ошибка: недопустимые символы в hex-строке'),
    ('0123456789АBCDEF', 0, 'Ошибка: недопустимые символы в hex-строке'),
    ('0x1234', 0, 'Ошибка: недопустимые символы в hex-строке'),
    ('DEFG', 0, 'Ошибка: недопустимые символы в hex-строке'),
    ('0123 4567', 0, 'Ошибка: недопустимые символы в hex-строке'),
    ('', 0, 'Ошибка: hex-строка слишком короткая (минимум 4 символа)'),
    ('012', 0, 'Ошибка: hex-строка слишком короткая (минимум 4 символа)'),
    ('0123456789ABCDEF' * 2 + 'F', 0, 'Ошибка: hex-строка слишком длинная (максимум 32 символа)')
], ids=[
    "start_bit_62",
    "start_bit_49",
    "negative_start_bit_minus_1",
    "min_length_invalid_bit",
    "max_length_invalid_bit",
    "wrong_symbols_generic",
    "special_char_exclamation",
    "russian_A_char",
    "hex_prefix_0x",
    "invalid_letters_DEFG",
    "space_inside_string",
    "empty_string_hex_string",
    "too_short_3_chars",
    "too_long_33_chars",
])
def test_error_cases(hex_str, start_bit, expected_error):
    assert getfield16(hex_str, start_bit) == expected_error
