X, Y = 13, 2


def generate_key_square(key):
    # Преобразование ключа в строку без пробелов и лишних символов
    key = key.replace(" ", "").lower()
    key = ''.join(filter(str.isalpha, key))

    # Создание алфавита из уникальных символов ключа
    alphabet = []
    for char in key:
        if char not in alphabet:
            alphabet.append(char)

    # Добавление оставшихся символов алфавита
    for char in range(ord('a'), ord('z') + 1):
        char = chr(char)
        if char not in alphabet:
            alphabet.append(char)

    # Формирование матрицы ключевого квадрата (XxY)
    key_square = [alphabet[i:i + X] for i in range(0, len(alphabet), X)]

    return key_square


def find_bigrampair(key_square, char):
    for i, row in enumerate(key_square):
        if char in row:
            return i, row.index(char)


def encrypt(text, key):
    # Преобразование текста в строку без пробелов и лишних символов
    text = text.replace(" ", "").lower()
    text = ''.join(filter(str.isalpha, text))

    # Добавление символа "X" в случае нечетного количества символов
    if len(text) % 2 != 0:
        text += "x"

    # Создание ключевого квадрата
    key_square = generate_key_square(key)

    # Разделение текста на биграммы и создание нового зашифрованного текста
    encrypted_text = ""
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1]

        row1, col1 = find_bigrampair(key_square, char1)
        row2, col2 = find_bigrampair(key_square, char2)

        # Обработка случаев, когда символы находятся на одной строке или столбце
        if row1 == row2:
            encrypted_text += key_square[row1][(col1 + 1) % X]
            encrypted_text += key_square[row2][(col2 + 1) % X]
        elif col1 == col2:
            encrypted_text += key_square[(row1 + 1) % X][col1]
            encrypted_text += key_square[(row2 + 1) % X][col1]
        else:
            encrypted_text += key_square[row1][col2]
            encrypted_text += key_square[row2][col1]

    return encrypted_text


def decrypt(text, key):
    # Преобразование текста в строку без пробелов и лишних символов
    text = text.replace(" ", "").lower()
    text = ''.join(filter(str.isalpha, text))

    # Добавление символа "X" в случае нечетного количества символов
    if len(text) % 2 != 0:
        text += "x"

    # Создание ключевого квадрата
    key_square = generate_key_square(key)

    # Разделение текста на биграммы и создание нового зашифрованного текста
    decrypted_text = ""
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1]

        row1, col1 = find_bigrampair(key_square, char1)
        row2, col2 = find_bigrampair(key_square, char2)

        # Обработка случаев, когда символы находятся на одной строке или столбце
        if row1 == row2:
            decrypted_text += key_square[row1][(col1 - 1) % X]
            decrypted_text += key_square[row2][(col2 - 1) % X]
        elif col1 == col2:
            decrypted_text += key_square[(row1 - 1) % X][col1]
            decrypted_text += key_square[(row2 - 1) % X][col1]
        else:
            decrypted_text += key_square[row1][col2]
            decrypted_text += key_square[row2][col1]

    return decrypted_text


def encrypt_file(filename: str, key: str):
    with open(filename, 'r') as fin:
        encrypted_text = encrypt(fin.read(), key)
    with open(f'{filename}_encrypted.txt', 'w+') as fout:
        print(encrypted_text, file=fout)


def decrypt_file(filename: str, key: str):
    with open(filename, 'r') as fin:
        decrypted_text = decrypt(fin.read(), key)
    with open(f'{filename}_decrypted.txt', 'w+') as fout:
        print(decrypted_text, file=fout)


# Пример
plaintext = "hello world"
key = "example"
encrypted_text = encrypt(plaintext, key)
print(encrypted_text)
decrypted_text = decrypt(encrypted_text, key)
print(decrypted_text)
