# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


def get_encryption(input_text, key):
    encrypt = ""
    for c in input_text:
        if c.isupper(): #проверить, является ли символ прописным
            c_index = ord(c) - ord('A')
            # сдвиг текущего символа на позицию key
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypt += c_new
        elif c.islower(): #проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypt += c_new
        elif c.isdigit():
            # если это число, сдвинуть его фактическое значение 
            c_new = (int(c) + key) % 10
            encrypt += str(c_new)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            encrypt += c
    return encrypt

def get_decryption(new_text, key):
    decrypt = ""
    for c in new_text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            # сдвинуть текущий символ влево на позицию клавиши, чтобы получить его исходное положение
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypt += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypt += c_og
        elif c.isdigit():
            # если это число, сдвиньте его фактическое значение 
            c_og = (int(c) - key) % 10
            decrypt += str(c_og)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            decrypt += c
    return decrypt

input_text = "Hello, World"
new_text = get_encryption(input_text, 1)
print("Plain text message:\n", input_text)
print("Encrypted new_text:\n", new_text)