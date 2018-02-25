# Söker efter modiferade filer enligt angivet datum.
# https://docs.python.org/3/library/time.html#module-time
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

"""
datum = convert_date_sec('24.02.2018')
a = modified_date('tests.py', datum)
print(a)
"""
