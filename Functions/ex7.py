# https://stackoverflow.com/questions/19007383/compare-two-different-files-line-by-line-in-python

def file_compare(filename_1, filename_2):
    """
    Input: filnamn 1, filnamn 2
    output: Returnerar vad som återfinns i filnamn 1 men inte i filnamn 2.

    Återgivande sker i form av lista där varje element är den rad som skiljer.
    Listan är ej ordnad, alltså rangordning reflekterar ej läst rad.
    """
    f1 = open(filename_1, 'r')
    f2 = open(filename_2, 'r')
    s_diff = set(f1).difference(f2)
    l_diff = list(s_diff)
    diff = []
    for i in l_diff:
        i = i.rstrip('\n')
        diff.append(i)
    return diff

"""test
a = file_compare('test1.txt', 'test2.txt')
print(a)
"""
