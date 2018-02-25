# Hittar och skriver ut filtyp funna i angiven mapp, inlusive undermappar.
# https://stackoverflow.com/questions/22714013/recursively-searching-for-files-with-specific-extensions-in-a-directory

def find_filetype(start_path, file_type):
    """
    Input: mapp eller directory, filtyp
    Output: Sorterad lista av funna eftersökta filtyper. Söker genom undermappar.
    """
    import os
    found = []
    for path, dirs, files in os.walk(start_path):
        for filename in files:
            if filename.endswith(file_type):
                found.append(os.path.join(path, filename))
    return sorted(found)

"""Test
a = (find_filetype('/', '.pdf'))
print(a)
for i in a:
    print(i)
"""
