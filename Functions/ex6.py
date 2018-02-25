def read_file_list(file_name):
    """
    Input: filnamn
    Output: list object med varje läst rad som element.
    """
    f = open(file_name, 'r')
    read_lines = []
    line = f.readline()
    while line != '':
        line = line.rstrip('\n')
        read_lines.append(line)
        line = f.readline()
    f.close()
    return read_lines

def write_file_list(file_name, content):
    """
    Input: filnamn som ska skrivas till, vad som ska skrivas
    Output: Skriver till filnamn varje list element för var rad.
    """
    f = open(file_name, 'w')
    for i in content:
        f.write(i + '\n')
    f.close

def encrypt(content, code):
    """
    Input: Lista av strängar som element, cypher i form av dictionary.
    Output: Ny lista av nya strängar som element enligt cypher.
    """
    new_line = ''
    new_content = []
    for i in content:
        for j in i:
            new_line += code[j]
        new_content.append(new_line)
        new_line = ''
    return new_content

def decrypt(content, code):
    """
    Input: Krypterade strängar i lista, cypher i form av dictionary.
    Output: Lista av strängar.
    """
    decode_code = {value: key for key, value in code.items()}
    new_line = ''
    new_content = []
    for i in content:
        for j in i:
            new_line += decode_code[j]
        new_content.append(new_line)
        new_line = ''
    return new_content

def en_de_crypt(file_name, mode):
    """
    Input: fil som ska krypteras/avkrypteras, mode:encrypt/decrypt
    Output: Skriver fil antingen filnamn.en eller filnamn.de
    https://stackoverflow.com/questions/40062728/cipher-encoder-in-python-using-dictionaries
    """
    code = {'3': 'N', 'j': 'B', 'w': 'l', 'f': 'Y', '0': 'h', 'A': 'u', 'h': 'n',
            'Å': ')', 'a': 'a', '<': 'z', 's': 'G', 'R': '>', '#': '&', 'Y': '7',
            'F': 'Ä', 'J': '1', 'Ö': 'k', 'M': 'd', 'd': 'ä', 'Z': 'F', '6': 'x',
            'X': 'X', 't': 't', 'Ä': 'I', '?': 'e', 'o': 'w', '&': 'y', 'k': 'W',
            'K': 'H', 'e': 'K', '!': 'Z', 'y': 'M', 'H': '¤', 'r': '/', ')': 'H',
            '4': '4', 'Q': '8', 'P': 'v', 'L': '3', 'G': 'r', '¤': 'b', 'S': 'ö',
            'v': 'T', 'D': '?', 'ö': 'g', 'u': 'Å', '7': 'j', 'B': 'f', 'I': 'R',
            'z': 'A', '2': 'Q', 'l': '6', '5': '5', 'p': 'c', 'V': 'i', '9': 'Ö',
            'U': 'D', 'n': 'å', '/': 'q', 'm': '9', 'b': 'o', 'T': 's', 'W': '!',
            '1': 'E', 'i': 'O', 'N': 'U', 'E': 'm', 'g': '0', 'å': '%', '%': 'p',
            'ä': 'C', '8': '#', '(': 'J', 'O': 'P', 'c': '+', '+': 'S', 'C': '<',
            'q': '2', '>': 'L', 'x': 'V', ' ': ' ', '=': '-', '{': '§', ':': ',',
            '\'': '\'', ',': '}', '}': '.', '[': '@', ']': '£', '_': '^', '.': '*'}

    if mode == 'encrypt':
        content = read_file_list(file_name)
        new_content = encrypt(content, code)
        new_file_name = file_name +'.en'
        write_file_list(new_file_name, new_content)

    elif mode == 'decrypt':
        content = read_file_list(file_name)
        new_content = decrypt(content, code)
        if '.en' in file_name:
            file_name = file_name.replace('.en', '')
        new_file_name = file_name + '.de'
        write_file_list(new_file_name, new_content)

"""test
en_de_crypt('test.py.en', 'decrypt')
"""
