# Funktioner för cli.py och gui.py

def directory_files(start_path):
    """
    Input: mapp eller directory
    Output: Sorterad lista av alla filer inklusive undermappar och dess filer.
    """
    import os
    list_files = []
    for path,dirs,files in os.walk(start_path):
        for filename in files:
            list_files.append(os.path.join(path,filename))
    return sorted(list_files)

def find_filetype(start_path, file_type):
    """
    Input: mapp eller directory, filtyp
    Output: Sorterad lista av funna eftersökta filtyper. Söker genom undermappar.
    """
    import os
    found = []
    if not file_type.startswith('.'):
        file_type = '.' + file_type
    print(file_type)
    for path, dirs, files in os.walk(start_path):
        for filename in files:
            if filename.endswith(file_type):
                found.append(os.path.join(path, filename))
    return sorted(found)

def convert_pdf(file_name):
    """
    Input: filnamn; .pdf
    Output: ny .txt fil av tidigare namn + .txt. Innehåll omvandlat till ASCII tecken,
    enligt GhostScript: ps2ascii
    """
    import os
    input = file_name
    output = file_name + '.txt'
    os.system(("ps2ascii %s %s") %(input, output))

def convert_doc(file_name):
    """
    Input: filnamn; .doc
    Output: ny .txt fil av tidigare namn + .txt. Innehåll omvandlat till ASCII tecken,
    enligt antiword (Linux).
    """
    import os
    os.system('antiword ' + str(file_name) + ' >' + str(file_name) + '.txt')

def convert_odt(file_name):
    """
    Input: filnamn; .odt
    Output: ny .txt fil av tidigare namn + .txt. Innehåll omvandlat till ASCII tecken,
    enligt odt2txt (Linux).
    """
    import os
    os.system('odt2txt ' + str(file_name) + ' >' + str(file_name) + '.txt')

def convert_docx(file_name):
    """
    Input: filnamn; .docx
    Output: ny .txt fil av tidigare namn + .txt. Innehåll omvandlat till ASCII tecken,
    enligt docx2txt (Linux).
    """
    import docx2txt
    doc = docx2txt.process(file_name)
    new_file = file_name + '.txt'
    f = open(new_file, 'w')
    f.write(doc)

def read_file_full(file_name):
    """
    Input: filnamn; den fil som ska läsas in.
    Output: Filens hela innehåll i en string.
    """
    f = open(file_name, 'r')
    content = f.read()
    return content

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

def read_and_find(file_name, information):
    """
    Input: filnamn, string som eftersöks i fil.
    Output: True om string påträffas i fil.
    """
    if file_name.endswith('.pdf'):
        convert_pdf(file_name)
        file_name = file_name + '.txt'
    elif file_name.endswith('.docx'):
        convert_docx(file_name)
        file_name = file_name + '.txt'
    elif file_name.endswith('.doc'):
        convert_doc(file_name)
        file_name = file_name + '.txt'
    elif file_name.endswith('.odt'):
        convert_odt(file_name)
        file_name = file_name + '.txt'

    read_lines = read_file_list(file_name)
    for i in read_lines:
        if information in i:
            return True

def find_info_in_filetype(start_path, file_type, information):
    """
    Input: mapp som söks, filtyp, eftersökt information som string.
    Output: Filer innehållande eftersökt string.
    """
    files = find_filetype(start_path, file_type)
    found = []
    for i in files:
        if read_and_find(i, information) == True:
            found.append(i)
    return found

def modified_date(path_file, m_date):
    """
    Input: fullständigt filnamn, datum vart efter fil kan ha modifierats.
    Output: Filnamn returneras om filen modifierats efter datum
    """
    import os
    import time
    t_modified = os.path.getmtime(path_file)
    if t_modified > m_date:
        date = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(t_modified))
        output = path_file + ' modified last at: ' + date
        return output

def convert_date_sec(given_date):
    """
    Input: datum i format: 24.02.2018
    Output: datum sedan epoch i sekunder
    """
    from datetime import datetime
    date_sec = datetime.strptime(given_date, '%d.%m.%Y')
    date_sec = date_sec.timestamp()
    return date_sec


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
            '\'': '\'', ',': '}', '}': '.', '[': '@', ']': '£', '_': '^', '.': '*',
            '-': '~'}

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

def file_diff(filename_1, filename_2):
    """
    Input: filnamn1, filnamn2
    Output: Returnerar en lista där var element är den rad som återfinns i filename_1 men
    ej i filename_2. Erhåller list ordning, vilket set annars ej gör.
    https://stackoverflow.com/questions/10005367/retaining-order-while-using-pythons-set-difference
    """
    f1 = read_file_list(filename_1)
    f2 = read_file_list(filename_2)
    diff = set(f1) - set(f2)
    result = [o for o in f1 if o in diff]
    return result

def get_hash(text):
    """
    Input: En string av text; En fils fullständiga innehåll i form av string.
    Output: Ett md5 hash värde beroende på innehåll
    referens:
    https://stackoverflow.com/questions/37991475/comparing-hashes-and-evaluate-each-hash
    """
    import hashlib

    a = hashlib.md5()
    a.update(text.encode('utf-8'))
    return a.hexdigest()

def eval_hash(hsh1, hsh2):
    """
    Input: första hash, andra hash.
    Output: True ifall hsh1 är detsamma som hsh2, annars False.
    """
    if hsh1 == hsh2:
        return True
    else:
        return False

def create_hashset(hsh, file_name):
    """
    Input: hash värde, filnamn på hashset
    Output: Skapar hashet av filnamn eller appenderar hash til fil.
    Var hash är en rad.
    """
    if check_file_exist(file_name) == True:
        f = open(file_name, 'a')
        f.write(hsh + '\n')
        f.close()
    elif check_file_exist(file_name) == False:
        f = open(file_name, 'w')
        f.write(hsh + '\n')
        f.close()

def check_file_exist(file_name):
    """
    Input: Filnamn.
    Output: True om fil finns och kan läsas. annars False.
    """
    try:
        f = open(file_name, 'r')
        f.read()
        f.close()
        return True
    except:
        return False

def get_hardware():
    """
    Kräver psutil för att bland annat läsa ram minne.
    https://github.com/giampaolo/psutil/blob/master/INSTALL.rst
    Windows kör diskperf -y
    http://psutil.readthedocs.io/en/latest/
    """
    import psutil
    import platform
    import datetime

    f_clock_speed = psutil.cpu_freq()[2] / 1000   # Mhz
    memory = psutil.virtual_memory()
    mem_tot = int(memory[0] / 1024 / 1024)
    user = psutil.users()[0]
    c_user = user[0]

    # output:
    user = c_user
    system = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    clock_speed = f_clock_speed
    memory_tot = mem_tot
    """Föreslaget format:
    print('User:             ', c_user)
    print('system:           ', platform.system())
    print('node:             ', platform.node())
    print('release:          ', platform.release())
    print('version:          ', platform.version())
    print('machine:          ', platform.machine())
    print('processor:        ', platform.processor())
    print('     clock speed: ', clock_speed, 'Ghz')
    print('memory:           ')
    print('     total:       ', mem_tot, 'MB')
    """
    return user, system, node, release, version, machine, processor, clock_speed, memory_tot


def get_hardware_less():
    """
    Endast inbyggda funktioner, ej psutil.
    """
    import platform
    import datetime

    # output:
    system = platform.system()
    node = platform.node()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    return system, node, release, version, machine, processor
