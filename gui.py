
import ftlib
from tkinter import *

# Ful lösning men enda sätt funnet för att kringå att tkinter körs vid import
def main_gui():
    # Allmän textbox konstant
    global textbox

    def raise_frame(frame):
        # Hanterar byte mellan frame, "ny sida"
    	frame.tkraise()

    def about_us():
        textbox.delete('1.0', END)
        textbox.insert(END, '\n' + '───▄▄▄' + '             Forensic Tool')
        textbox.insert(END, '\n' + '─▄▀░▄░▀▄' + '           DI-2006')
        textbox.insert(END, '\n' + '─█░█▄▀░█')
        textbox.insert(END, '\n' + '─█░█▄▀░█' + '           Pontus Hedman, ')
        textbox.insert(END, '\n' + '─█░▀▄▄▀█▄█▄▀' + '       Gustav Helgesson,')
        textbox.insert(END, '\n' + '▄▄█▄▄▄▄███▀' + '        Niklas Englund')
        textbox.insert(END, '\n' + '\nFöljande funktioner:')
        textbox.insert(END, '\n' + '1. Utforska angiven mapp, inklusive undermappar. Erhållna filer kan begränsas till efter filtyp. Vidare begränsning kan göras där endast filer modifierade efter angivet datum visas.')
        textbox.insert(END, '\n' + '\n2. Sök fil innehållande del av angiven text information. Endast stöd för plaintext eller följande filtyper: .pdf, .doc, .docx, .odt. ')
        textbox.insert(END, '\n' + '\n3. Filkryptering. Skapa en krypterad kopia av angiven fil. Krypterad kopia erhåller filformat: .en. Endast .en filer kan dekrypteras, fil av samma namn med filformat: .de skapas.')
        textbox.insert(END, '\n' + '\n4. Jämför filer. Två filers innehåll jämförs med varandra, där vad som beträffas i första fil men ej i andra fil skrivs ut. För att få information om det omvända, byt plats på filnamn.')
        textbox.insert(END, '\n' + '\n5. md5 hashning. Erhåll md5 hashvärde på angiven fil. Jämför erhållet hashvärde med angivet värde. Jämför erhållet hashvärde med hashvärden som läses från en fil med hashvärden.')
        textbox.insert(END, '\n' + '\n6. Systeminformation. Skriv ut information om den dator denna program körs på. Återfinns ej psutil på datorn skrivs ej information om användare, processorhastighet, och minne.')
        textbox.insert(END, '\n' + '\n7. About. Denna sida.')

    def tool_1():
        # Filutforskare
        # Raderar tidigare information i textbox
        textbox.delete('1.0', END)
        start_path = t1_entry.get()
        given_date = t2_entry.get()
        given_file_type = t12_entry.get()
        modified_files = []

        try:
            files = ftlib.directory_files(start_path)
        except:
            textbox.insert(END, '\n' + 'Ogiltig filväg!')

        if given_date != '':
            try:
                m_date = ftlib.convert_date_sec(given_date)
            except:
                textbox.insert(END, '\n' + 'Ogiltigt datum!')

            for i in files:
                try:
                    modified_files.append(ftlib.modified_date(i, m_date))
                except:
                    textbox.insert(END, '\n' + 'Ogiltigt datum!')

        if given_file_type == '':
            if given_date == '':
                for i in files:
                    textbox.insert(END,'\n' + i)
            else:
                for i in modified_files:
                    if i != None:
                        textbox.insert(END, '\n' + i)

        elif given_file_type != '':
            modified_files_by_type = []
            files = ftlib.find_filetype(start_path, given_file_type)

            if given_date == '':
                for i in files:
                    textbox.insert(END, '\n' + i)
            else:
                for i in files:
                    modified_files_by_type.append(ftlib.modified_date(i, m_date))
                for i in modified_files_by_type:
                    if i != None:
                        textbox.insert(END, '\n' + i)

    def tool_2():
        # Söker efter fil
        textbox.delete('1.0', END)

        start_path = t3_entry.get()
        file_type = t4_entry.get()
        information = t5_entry.get()

        try:
            files = ftlib.find_info_in_filetype(start_path, file_type, information)
        except:
            textbox.insert(END, '\n' + 'Kan ej konvertera och läsa ' + str(file_type) + '. Detta program nyttjar följande program för konvertering av de filtyper som stöds: ')
            textbox.insert(END, '\n' + '.pdf: ps2ASCII, .doc: Antiword, docx: docx2txt, odt: odt2txt.')

        if files != []:
            textbox.insert(END, '\n' + 'Del av string återfinns i följande filer: ')
            for i in files:
                textbox.insert(END, '\n' + i)
        else:
            textbox.insert(END, '\n' + 'Ingen träff! Se över inmatade värden.')

    def tool_3_crypt():
        # Filkryptering
        textbox.delete('1.0', END)
        file_name = t6_entry.get()
        try:
            ftlib.en_de_crypt(file_name, 'encrypt')
            textbox.insert(END, '\n' + file_name + '.en återfinns i den mapp detta program körs.')
        except:
            textbox.insert(END, '\n' + 'Kan ej kryptera fil.')

    def tool_3_decrypt():
        # Fildekryptering
        textbox.delete('1.0', END)
        file_name = t6_entry.get()
        if file_name.endswith('.en'):
            try:
                ftlib.en_de_crypt(file_name, 'decrypt')
                textbox.insert(END, '\n' + file_name[:-3] + '.de återfinns i den mapp detta program körs.')
            except:
                textbox.insert(END, '\n' + 'Ogiltig filväg!')
        else:
            textbox.insert(END, '\n' + 'Fil är ej av filtyp .en.')

    def tool_4():
        # Jämför två filer. Vad som beträffas i fil 1 men ej i fil 2 skrivs ut.
        textbox.delete('1.0', END)
        filename_1 = t7_entry.get()
        filename_2 = t8_entry.get()

        try:
            unique_f1 = ftlib.file_diff(filename_1, filename_2)
            textbox.insert(END, '\n' + filename_1 + ' innehåller följande rader som ej återfinns i ' + filename_2 + ': ')

            for i in unique_f1:
                textbox.insert(END, '\n' + i)
        except:
            textbox.insert(END, '\n' + 'Kan ej läsa fil!')


    def tool_5_gethash():
        # Erhåller md5 hash av fil
        textbox.delete('1.0', END)
        file_name = t9_entry.get()
        try:
            text = ftlib.read_file_full(file_name)
            hsh = ftlib.get_hash(text)
            textbox.insert(END, '\n' + file_name + ' har följande md5 hashvärde: ')
            textbox.insert(END, '\n' + str(hsh))
        except:
            textbox.insert(END, '\n' + 'Kan ej läsa fil!')

    def tool_5_evalhash():
        # Jämför md5 hash av fil med angivet värde.
        textbox.delete('1.0', END)
        file_name = t9_entry.get()
        known_hsh = t10_entry.get()
        try:
            text = ftlib.read_file_full(file_name)
            hsh = ftlib.get_hash(text)
            if ftlib.eval_hash(hsh, known_hsh) == True:
                textbox.insert(END, '\n' + 'True! Hashvärde av båda filer är identiska.')
            elif ftlib.eval_hash(hsh, known_hsh) == False:
                textbox.insert(END, '\n' + 'False! Hashvärde av båda filer är olika.')
        except:
            textbox.insert(END, '\n' + 'Kan ej läsa fil!')

    def tool_5_evalhashfile():
        # Jämför md5 hash av fil med en fil av hashvärden.
        textbox.delete('1.0', END)
        file_name = t9_entry.get()
        file_name_hashes = t11_entry.get()
        try:
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
                textbox.insert(END, '\n' + 'md5 hashvärde: \n' + hsh)
                textbox.insert(END, '\n' + 'Återfinns i: ' + file_name_hashes)
            else:
                textbox.insert(END, '\n' + 'md5 hashvärde: \n' + hsh)
                textbox.insert(END, '\n' + 'Återfinns EJ i: ' + file_name_hashes)
        except:
            textbox.insert(END, '\n' + 'Kan ej läsa fil!')

    def tool_6():
        # Skriver ut systeminformation. Mest information erhålls
        # om man har support för psutil installerat.
        textbox.delete('1.0', END)
        try:
            sysinfo = ftlib.get_hardware()
            clock_speed = str(sysinfo[7])
            ram = str(round(sysinfo[8] / 1000))

            textbox.insert(END, '\n' + 'Användare:         ' + sysinfo[0])
            textbox.insert(END, '\n' + 'Operativ system:   ' + sysinfo[1])
            textbox.insert(END, '\n' + 'Datornamn:         ' + sysinfo[2])
            textbox.insert(END, '\n' + 'Utgåva:            ' + sysinfo[3])
            textbox.insert(END, '\n' + 'Version:           ' + sysinfo[4])
            textbox.insert(END, '\n' + 'Systemtyp:         ' + sysinfo[5])
            textbox.insert(END, '\n' + 'Processor:         ' + sysinfo[6] + ' CPU @ ' + clock_speed + ' Ghz')
            textbox.insert(END, '\n' + 'Installerat RAM:   ' + ram + ' GB')
        except:
            # Om man ej har psutil
            textbox.insert(END, '\n' + 'psutil för mer information.')
            sysinfo = ftlib.get_hardware_less()

            textbox.insert(END, '\n' + 'Användare:         ' + 'N/A')
            textbox.insert(END, '\n' + 'Operativ system:   ' + sysinfo[0])
            textbox.insert(END, '\n' + 'Datornamn:         ' + sysinfo[1])
            textbox.insert(END, '\n' + 'Utgåva:            ' + sysinfo[2])
            textbox.insert(END, '\n' + 'Version:           ' + sysinfo[3])
            textbox.insert(END, '\n' + 'Systemtyp:         ' + sysinfo[4])
            textbox.insert(END, '\n' + 'Processor:         ' + sysinfo[5] + ' CPU @ ' + 'N/A' + ' Ghz')
            textbox.insert(END, '\n' + 'Installerat RAM:   ' + 'N/A' + ' GB')

    root = Tk()
    root.title('Forensic Tool')

    # Sidor
    f1 = Frame(root)	# Startskärm
    f2 = Frame(root)	# kataloginnehåll + filtyp + modifikation datum
    f3 = Frame(root)    # text i fil
    f4 = Frame(root)	# Filkryptering
    f5 = Frame(root)	# Jämför filer
    f6 = Frame(root)	# Hantering av filhash

    for frame in (f1, f2, f3, f4, f5, f6):
    	frame.grid(row = 0, column = 2, sticky = 'news')

    # sida 1: Startskärm
    textbox = Text(root, height = 16, width = 40)
    textbox.grid(row=0, column = 0, rowspan = 6)

    sb = Scrollbar(root, command = textbox.yview)
    sb.grid(row = 0, column = 1, rowspan = 6, sticky = 'nsew')
    textbox.configure(yscrollcommand = sb.set)

    button = Button(f1, text = 'Utforska', width = 30, command = lambda: raise_frame(f2))
    button.grid(row = 2)

    button = Button(f1, text = 'Sök fil', width = 30, command = lambda: raise_frame(f3))
    button.grid(row = 3)

    button = Button(f1, text = 'Filkryptering', width = 30, command = lambda: raise_frame(f4))
    button.grid(row = 4)

    button = Button(f1, text = 'Jämför filer', width = 30, command = lambda: raise_frame(f5))
    button.grid(row = 5)

    button = Button(f1, text = 'Hantering av filhash', width = 30, command = lambda: raise_frame(f6))
    button.grid(row = 6)

    button = Button(f1, text = 'Systeminformation', width = 30, command = lambda: tool_6())
    button.grid(row = 7)

    button = Button(f1, text = 'About', width = 30, command = lambda: about_us())
    button.grid(row = 8)

    button = Button(f1, text = 'Avsluta program', width = 30, command = lambda: exit())
    button.grid(row = 9)

    # sida 2: kataloginnehåll + filtyp
    pdf = IntVar()
    doc = IntVar()
    docx = IntVar()
    odt = IntVar()

    Label(f2, text = "Absolut filväg till mapp: ").grid(row = 0, sticky = W)
    t1_entry = Entry(f2)
    t1_entry.grid(row = 1, sticky = W)


    Label(f2, text = "Begränsa filtyp: ").grid(row = 2, sticky = W)
    t12_entry = Entry(f2)
    t12_entry.grid(row = 3, sticky = W)

    Label(f2, text = "Begränsa efter datum (15.12.2018):").grid(row = 5, sticky = W)
    t2_entry = Entry(f2)
    t2_entry.grid(row = 6, sticky = W)

    button = Button(f2, text = 'Utforska mapp', width = 30, command = tool_1)
    button.grid(row = 7, pady = (8, 0))

    button = Button(f2, text = 'Tillbaka', width = 30, command = lambda: raise_frame(f1))
    button.grid(row = 8)

    # sida 3: text i fil
    Label(f3, text = "Kan endast konvertera: .pdf, .doc, .docx, .odt").grid(row = 0, sticky = W)
    Label(f3, text = "Absolut filväg till mapp: ").grid(row = 1, sticky = W)
    t3_entry = Entry(f3)
    t3_entry.grid(row = 2, sticky = W)

    Label(f3, text = "Filtyp: ").grid(row = 3, sticky = W)
    t4_entry = Entry(f3)
    t4_entry.grid(row = 4, sticky = W)

    Label(f3, text = "Information som eftersöks i fil:").grid(row = 5, sticky = W)
    t5_entry = Entry(f3)
    t5_entry.grid(row = 6, sticky = W)

    button = Button(f3, text = 'Sök', width = 30, command = tool_2)
    button.grid(row = 7, pady = (8, 0), sticky = W)

    button = Button(f3, text = 'Tillbaka', width = 30, command = lambda: raise_frame(f1))
    button.grid(row = 8, sticky = W)

    # sida 4: Filkryptering
    Label(f4, text = "Kan endast dekryptera fil av ändelse: .de").grid(row = 2, sticky = W)
    Label(f4, text = "Absolut filväg: ").grid(row = 0, sticky = W)
    t6_entry = Entry(f4, width = 32)
    t6_entry.grid(row = 1)

    button = Button(f4, text = 'Kryptera', width = 13, command = tool_3_crypt)
    button.grid(row = 3, sticky = W)

    button = Button(f4, text = 'Dekryptera', width = 13, command = tool_3_decrypt)
    button.grid(row = 3, sticky = E)

    button = Button(f4, text = 'Tillbaka', width = 30, command = lambda: raise_frame(f1))
    button.grid(row = 7, pady = (8, 0))

    # sida 5: Jämför filer
    Label(f5, text = "Skriver vad som återträffas i fil 1 men ej i fil 2").grid(row = 0, sticky = W)
    Label(f5, text = "Fil 1: ").grid(row = 1, sticky = W)
    t7_entry = Entry(f5, width = 32)
    t7_entry.grid(row = 2, sticky = W)

    Label(f5, text = "Fil 2: ").grid(row = 3, sticky = W)
    t8_entry = Entry(f5, width = 32)
    t8_entry.grid(row = 4, sticky = W, pady = (0, 7))

    button = Button(f5, text = 'Jämför', width = 30, command = tool_4)
    button.grid(row = 5, sticky = W)

    button = Button(f5, text = 'Tillbaka', width = 30, command = lambda: raise_frame(f1))
    button.grid(row = 8, sticky = W)

    # sida 6: Hantering av filhash
    Label(f6, text = "Fil: ").grid(row = 0, sticky = W)
    t9_entry = Entry(f6, width = 15)
    t9_entry.grid(row = 1, sticky = W)

    button = Button(f6, text = 'md5 Hash', width = 12, command = tool_5_gethash)
    button.grid(row = 1, sticky = E)

    Label(f6, text = "Hashvärde: ").grid(row = 2, sticky = W)
    t10_entry = Entry(f6, width = 15)
    t10_entry.grid(row = 3, sticky = W)

    button = Button(f6, text = 'Jämför', width = 12, command = tool_5_evalhash)
    button.grid(row = 3, sticky = E)

    Label(f6, text = "Fil med hashvärden: ").grid(row = 4, sticky = W)
    t11_entry = Entry(f6, width = 15)
    t11_entry.grid(row = 5, sticky = W)

    button = Button(f6, text = 'Jämför', width = 12, command = tool_5_evalhashfile)
    button.grid(row = 5, sticky = E, pady = (0, 9))

    button = Button(f6, text = 'Tillbaka', width = 30, command = lambda: raise_frame(f1))
    button.grid(row = 8)

    # Main
    raise_frame(f1)
    about_us()
    root.mainloop()

if __name__ == "__main__":
    main_gui()
