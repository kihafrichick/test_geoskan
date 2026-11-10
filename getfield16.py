import sys

def is_valid_hex_char(c):
    return c in '0123456789abcdefABCDEF'

def hex_char_to_int(c):
    return int(c, 16)

def int_to_hex_char(val):
    return format(val, 'X')

def getfield16(hex_str, start_bit):

    if len(hex_str) > 32:
        return "Ошибка: hex-строка слишком длинная (максимум 32 символа)"

    if len(hex_str) < 4:
        return "Ошибка: hex-строка слишком короткая (минимум 4 символа)"

    for c in hex_str:
        if not is_valid_hex_char(c):
            return "Ошибка: недопустимые символы в hex-строке"

    bits = ""
    for c in hex_str:
        val = hex_char_to_int(c)
        bits += format(val, '04b')

    total_bits = len(bits)

    if start_bit < 0 or start_bit + 16 > total_bits:
        return "Ошибка: некорректный стартовый бит"

    extracted = bits[start_bit:start_bit + 16]

    result = ""
    for i in range(0, 16, 4):
        chunk = extracted[i:i + 4]
        val = int(chunk, 2)
        result += int_to_hex_char(val)
    return result


if __name__ == "__main__":

    hex_str = input("Введите hex-строку: ").strip()
    start_bit_str = input("Введите номер стартового бита: ").strip()

    try:
        start_bit = int(start_bit_str)
    except ValueError:
        print("Ошибка: стартовый бит должен быть целым числом")
        sys.exit(1)

    result = getfield16(hex_str, start_bit)

    if result.startswith("Ошибка"):
        print(result)
        sys.exit(1)

    print("Результат:", result)