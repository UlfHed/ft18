
def make_cipher():
    """
    Skapar en dictionary med slumpade keys och slumpade värden.
    """
    import random
    keys = values = []
    symbols = 'abcdefghijklmnopqrstuvwxyzåäöABCDEFGHHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!#¤%&/(?+<>)}.,-_{'
    for i in symbols:
        keys.append(i)
    keys = random.sample(keys, len(keys))
    values = random.sample(values, len(values))
    d = dict(zip(keys, values))
    return d

def write_file(file_name, content):
    """
    Input: filnamn som ska skapas, vad som ska skrivas.
    """
    f = open(file_name, 'w')
    f.write(content)
    f.close()

write_file('cipher.txt', str(make_cipher()))
