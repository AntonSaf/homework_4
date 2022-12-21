# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# файл первый:

# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool

# файл второй:

# 12A11B10C6D5E4FG python is s7o c7ol

# Первая функция - текст зашифровывает
# Вторая - расшифровывает
# Две промежуточные - считывают с файла и записывают в файл


with open('file_encode.txt', 'w') as data:
    data.write('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))
print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')