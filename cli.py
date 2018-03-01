# Detta program nyttjar funktioner skrivna i ftlib.py.
import ftlib

def menu_generic():
    print('# '* 17)
    print('#     Alternativ:               #')
    print('#     1. Skriv till konsol.     #')
    print('#     2. Tillbaka.              #')
    print('# '* 17)

def menu_cipher():
    print('# ' * 16)
    print('#      Alternativ:            #')
    print('#      1. Kryptera fil.       #')
    print('#      2. Dekryptera fil.     #')
    print('#      3. Tillbaka.           #')
    print('# ' * 16)

def menu_welcome():
    print('# ' * 21)
    print('#     CLI - Forensic Tool - DI2006      #')
    print('#     Alternativ:                       #')
    print('#     1. Se funktioner.                 #')
    print('#     2. Avsluta program.               #')
    print('# ' * 21)

def menu_hash():
    print('# ' * 31)
    print('#      Detta program använder md5 som hashfunktion.         #')
    print('#      Alternativ:                                          #')
    print('#      1. Erhåll hashvärde av fil.                          #')
    print('#      2. Jämför hashvärde av fil med ett hashvärde.        #')
    print('#      3. Jämför hashvärde av fil med kända hashsummor.     #')
    print('#      4. Tillbaka.                                         #')
    print('# ' * 31)

def menu_tools():
    print('# ' * 34)
    print('#      Följande funktioner finns tillgängliga:                    #')
    print('#      Alternativ:                                                #')
    print('#      1. Finn filer inom angiven mapp.                           #')
    print('#      2. Finn filer av en angiven filtyp.                        #')
    print('#      3. Finn filer innehållande del av angiven information.     #')
    print('#      4. Finn filer som modifierats efter angivet datum.         #')
    print('#      5. Kryptera / avkryptera fil.                              #')
    print('#      6. Jämför innehåll i två text filer.                       #')
    print('#      7. Hashsummor.                                             #')
    print('#      8. Systeminformation.                                      #')
    print('#      9. Tillbaka.                                               #')
    print('# ' * 34)

def choice(section):
    if section == '2':
        prompt = 'Välj[1-2]: '
        limit_choice = 3

    if section == '3':
        prompt = 'Välj[1-3]: '
        limit_choice = 4

    elif section == '4':
        prompt = 'Välj[1-4]: '
        limit_choice = 5

    elif section == '9':
        prompt = 'Välj[1-9]: '
        limit_choice = 10

    while True:
        try:
            choice = int(input(prompt))
            if choice > 0 and choice < limit_choice:
                break
        except:
            print('Var god ange 1-' + section + '.')
    return choice

def tool_1():
    while True:
        menu_generic()
        cho_tool1 = choice('2')
        if  cho_tool1 == 1:
            while True:
                try:
                    start_path = input('Ange absolut filväg: ')
                    break
                except:
                    print('Var god ange filväg till den mapp som ska sökas.')

            files = ftlib.directory_files(start_path)
            if files != []:
                print('')
                print('Följande filer funna: ')
                for i in files:
                    print(i)
            else:
                print('')
                print('Ingen träff!')

        elif cho_tool1 == 2:
            break

def tool_2():
    while True:
        menu_generic()
        cho_tool2 = choice('2')
        if cho_tool2 == 1:
            while True:
                try:
                    file_type = input('Ange filändelse inklusive punkt: ')
                    break
                except:
                    print('Var god ange filändelse, t.ex. .pdf.')

            print('Ange den mapp som ska sökas i.')
            while True:
                try:
                    start_path = input('Ange absolut filväg: ')
                    break
                except:
                    print('Var god ange filväg till den mapp som ska sökas.')

            files = ftlib.find_filetype(start_path, file_type)
            if files != []:
                print('')
                print('Följande filer funna: ')
                for i in files:
                    print(i)
            else:
                print('')
                print('Ingen träff!')

        elif cho_tool2 == 2:
            break

def tool_3():
    while True:
        menu_generic()
        cho_tool3 = choice('2')
        if cho_tool3 == 1:
            while True:
                try:
                    file_type = input('Ange filändelse inklusive punkt: ')
                    break
                except:
                    print('Var god ange filändelse, t.ex. .pdf.')

            print('Ange den mapp som ska sökas i.')
            while True:
                try:
                    start_path = input('Ange absolut filväg: ')
                    break
                except:
                    print('Var god ange filväg till den mapp som ska sökas.')

            while True:
                try:
                    information = input('Ange det som söks efter: ')
                    break
                except:
                    print('Var god ange vad som söks efter.')

            files = ftlib.find_info_in_filetype(start_path, file_type, information)
            if files != []:
                print('')
                print('String:', information, 'återfinns i följande filer: ')
                for i in files:
                    print(i)
            else:
                print('')
                print('Ingen träff!')

        elif cho_tool3 == 2:
                break

def tool_4():
    import re
    while True:
        menu_generic()
        cho_tool4 = choice('2')
        if cho_tool4 == 1:
            print('Ange den mapp som ska sökas i.')
            while True:
                try:
                    start_path = input('Ange absolut filväg: ')
                    break
                except:
                    print('Var god ange filväg till den mapp som ska sökas.')

            print('Ange datum var efter ändring bör skett, ex. 24.02.2018.')
            while True:
                try:
                    given_date = input('Datum: ')
                    if re.match(r'[0-3][0-9].[0-1][0-9].20\d{2}', given_date) != None:
                        # Beränsar dagar till ^31 och månader ^12.
                        if int(given_date[0] + given_date[1]) < 32:
                            if int(given_date[3] + given_date[4]) < 13:
                                break
                    else:
                        print('Var god ange datum enligt 24.02.2018.')
                except:
                    print('Var god ange datum enligt 24.02.2018.')

            # Fångar ValueError i timedate funktionen
            try:
                m_date = ftlib.convert_date_sec(given_date)
            except:
                print('Ogiltigt datum!')

            files = ftlib.directory_files(start_path)
            m_files = []
            for i in files:
                m_files.append(ftlib.modified_date(i, m_date))

            if m_files != []:
                print('')
                print('Följande filer har modifierats efter ' + str(given_date) + '.')
                for i in m_files:
                    if i != None:   # Lista av modifierade filer, funktion returnerar None object för alla andra filer.
                        print(i)

        elif cho_tool4 == 2:
                break

def tool_5():
    while True:
        menu_cipher()
        cho_tool5 = choice('3')
        if cho_tool5 == 1:
            print('Ange fullständigt filnamn för att skapa en krypterad kopia.')
            while True:
                try:
                    file_name = input('filnamn: ')
                    break
                except:
                    print('Var god ange fullständigt filnamn.')

            ftlib.en_de_crypt(file_name, 'encrypt')
            print('')
            print(file_name + '.en återfinns i den mapp detta program körs.')

        elif cho_tool5 == 2:
            print('Ange fullständigt filnamn på den krypterade filen.')
            while True:
                try:
                    file_name = input('filnamn: ')
                    if file_name.endswith('.en'):
                        break
                    else:
                        print('Var god ange en fil med filändelse .en.')
                except:
                    print('Var god ange en fil med filändelse .en.')

            ftlib.en_de_crypt(file_name, 'decrypt')
            print('')
            # Slice till skäl av formatering, hanteras redan internt i modul.
            print(file_name[:-3] + '.de återfinns i den mapp detta program körs.')

        elif cho_tool5 == 3:
            break

def tool_6():
    while True:
        menu_generic()
        cho_tool6 = choice('2')
        if cho_tool6 == 1:
            print('Ange namn på första filen.')
            while True:
                try:
                    filename_1 = input('Fil 1: ')
                    break
                except:
                    print('Var god ange fullständigt filnamn.')

            print('Ange namn på andra filen.')
            while True:
                try:
                    filename_2 = input('fil 2: ')
                    break
                except:
                    print('Var god ange fullständigt filnamn.')

            unique_f1 = ftlib.file_diff(filename_1, filename_2)
            unique_f2 = ftlib.file_diff(filename_2, filename_1)

            print('')
            print(filename_1 + ' innehåller följande rader som ej återfinns i ' + filename_2 + '.')
            for i in unique_f1:
                print(i)
            print('')
            print(filename_2 + ' innehåller följande rader som ej återfinns i ' + filename_1 + '.')
            for i in unique_f2:
                print(i)

        elif cho_tool6 == 2:
            break

def tool_7():
    while True:
        menu_hash()
        cho_tool7 = choice('4')
        if cho_tool7 == 1:
            print('Ange fullständigt filnamn.')
            while True:
                try:
                    file_name = input('Filnamn: ')
                    break
                except:
                    print('Ange fullständigt filnamn.')

            text = ftlib.read_file_full(file_name)
            hsh = ftlib.get_hash(text)
            print('')
            print(file_name + ' har följande md5 hashvärde: ')
            print('md5 hash: ' + str(hsh))

        elif cho_tool7 == 2:
            print('Ange fullständigt filnamn.')
            while True:
                try:
                    file_name = input('Filnamn: ')
                    break
                except:
                    print('Ange fullständigt filnamn.')

            print('Mata in ett känt md5 hashvärde.')
            while True:
                try:
                    known_hsh = input('Ange md5 hashvärde: ')
                    break
                except:
                    print('Ange ett md5 hashvärde.')

            text = ftlib.read_file_full(file_name)
            hsh = ftlib.get_hash(text)
            if ftlib.eval_hash(hsh, known_hsh) == True:
                print('')
                print('True! Hashvärde av båda filer är identiska.')
            elif ftlib.eval_hash(hsh, known_hsh) == False:
                print('')
                print('False! Hashvärde av båda filer är olika.')

        elif cho_tool7 == 3:
            print('Ange fullständigt filnamn.')
            while True:
                try:
                    file_name = input('Filnamn: ')
                    break
                except:
                    print('Ange fullständigt filnamn.')

            print('Ange fullständigt filnamn på fil innehållande hashsummor.')
            while True:
                try:
                    file_name_hashes = input('Filnamn: ')
                    break
                except:
                    print('Ange fullständigt filnamn.')

            text = ftlib.read_file_full(file_name)
            hsh = str(ftlib.get_hash(text))
            hashes = ftlib.read_file_list(file_name_hashes)
            found_hashes = []

            # Görs på detta vis med found_hashes till skäl av formatering.
            # Iteration över tomma rader kan leda till missgynnande skrivna rader.
            for i in hashes:
                if ftlib.eval_hash(hsh, i) == True:
                    found_hashes.append(i)
            if found_hashes != []:
                print('')
                print('md5 hashvärde: ' + hsh + ' av ' + file_name + ' ÅTERFINNS i ' + file_name_hashes + '.')
            else:
                print('')
                print('md5 hashvärde: ' + hsh + ' av ' + file_name + ' återfinns EJ! i ' + file_name_hashes + '.')

        elif cho_tool7 == 4:
            break

def tool_8():
    while True:
        menu_generic()
        cho_tool8 = choice('2')
        if cho_tool8 == 1:
            sysinfo = ftlib.get_hardware()
            print('')
            print('Användare:                 ', sysinfo[0])
            print('Operativ system:           ', sysinfo[1])
            print('Datornamn:                 ', sysinfo[2])
            print('Utgåva:                    ', sysinfo[3])
            print('Version:                   ', sysinfo[4])
            print('Systemtyp:                 ', sysinfo[5])
            print('Processor:                 ', sysinfo[6], 'CPU @', sysinfo[7], 'Ghz')
            print('Installerat RAM:           ', round(sysinfo[8] / 1000), 'GB')
            print('')

        elif cho_tool8 == 2:
            break

def main_cli():
    while True:
        menu_welcome()
        cho_wel = choice('2')
        if cho_wel == 1:
            while True:
                menu_tools()
                cho_tol = choice('9')
                if cho_tol == 1:
                    tool_1()
                elif cho_tol == 2:
                    tool_2()
                elif cho_tol == 3:
                    tool_3()
                elif cho_tol == 4:
                    tool_4()
                elif cho_tol == 5:
                    tool_5()
                elif cho_tol == 6:
                    tool_6()
                elif cho_tol == 7:
                    tool_7()
                elif cho_tol == 8:
                    tool_8()
                elif cho_tol == 9:
                    break

        elif cho_wel == 2:
            break

# Används ej då forensictool.py används.
#main_cli()
