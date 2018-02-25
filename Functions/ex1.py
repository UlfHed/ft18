# Hittar alla filer i angiven mapp, inklusive undermappar.
# https://stackoverflow.com/questions/2759323/how-can-i-list-the-contents-of-a-directory-in-python

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

"""Test av Funktion
a = directory_files('full_path')
print(a, len(a))
for i in a:
    print(i)
"""
#test
