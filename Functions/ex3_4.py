# Söker efter angiven information i en viss typ av fil. Returnerar alla filnamn
# som innehåller informationen.
# https://stackoverflow.com/questions/15583535/how-to-extract-text-from-a-pdf-file-in-python
# https://stackoverflow.com/questions/44741226/converting-docx-to-pure-text
# https://github.com/ankushshah89/python-docx2txt
# Omvandlar följande: pdf, doc, docx, odt,
# Kräver följande:
# Linux: 'ps2ascii', 'antiword', 'odt2txt', 'docx2txt'
# Windows: 'pdftotext'


# Omvandlar pdf till txt; läsbart format.
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

# Kräver antiword; linux: sudo apt install antiword.
def convert_doc(file_name):
    """
    Input: filnamn; .doc
    Output: ny .txt fil av tidigare namn + .txt. Innehåll omvandlat till ASCII tecken,
    enligt antiword (Linux).
    """
    import os
    os.system('antiword ' + str(file_name) + ' >' + str(file_name) + '.txt')

# Kräver odt2txt; linux: sudo apt install odt2txt
def convert_odt(file_name):
    """
    Input: filnamn; .odt
    Output: ny .txt fil av tidigare namn + .txt. Innehåll omvandlat till ASCII tecken,
    enligt odt2txt (Linux).
    """
    import os
    os.system('odt2txt ' + str(file_name) + ' >' + str(file_name) + '.txt')

# Kräver docx2txt; linux: sudo apt install docx2txt
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

# Läser angiven fil, returnerar list object med varje läst rad som element.
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

# Kallar read_lines, söker efter 'information' i string; Påträffas 'information',
# returnerar True.
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

# Söker recursivt från angiven mapp efter filer av angivet filformat.
def find_filetype(start_path, file_type):
    """
    Input: mapp eller directory, filtyp
    Output: Sorterad lista av funna filer av eftersökt filtyp. Inklusive undermappar.
    """
    import os
    found = []
    for path, dirs, files in os.walk(start_path):
        for file_name in files:
            if file_name.endswith(file_type):
                found.append(os.path.join(file_name))
    return sorted(found)

# Kallar find_filetype(), sedan read_and_find(), återfinns fil med information
# returnerar denna funktion en lista av alla de filer.
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

"""test
a = find_info_in_filetype('.', '.docx', 'test')
print(a)
"""
