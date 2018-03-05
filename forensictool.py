def welcome():
    print('# ' * 17)
    print('#     Forensic Tool - DI2006    #')
    print('#     Alternativ:               #')
    print('#     1. Kör program i CLI      #')
    print('#     2. Kör program i GUI      #')
    print('#     3. Avsluta program.       #')
    print('# ' * 17)

def choose():
    while True:
        try:
            choice = int(input('Välj[1-3]: '))
            if choice > 0 and choice < 4:
                break
        except:
            print('Var god ange 1-3.')
    return choice

def check_1arg():
    import sys
    count_arg = 0
    for i in sys.argv[1:]:
        count_arg += 1
    if count_arg == 1:
        return True
    else:
        return False

def check_0arg():
    import sys
    count_arg = 0
    for i in sys.argv[1:]:
        count_arg += 1
    if count_arg == 0:
        return True
    else:
        return False

def main():
    # Filer för gränsnitt
    import cli
    import gui
    import sys

    if check_1arg() == True:
        arg = sys.argv[1]
        if arg.lower() in ['txt', 'text', 'cli']:
            cli.main_cli()
        elif arg.lower() == 'gui':
            gui.main_gui()
        else:
            print('')
            print('Följande argument tillgängliga:')
            print('Text program: txt, text, cli')
            print('Grafiskt program: gui')

    elif check_0arg() == True:
        while True:
            welcome()
            choice = choose()
            if choice == 1:
                cli.main_cli()
            elif choice == 2:
                gui.main_gui()
            elif choice == 3:
                break
    else:
        print('')
        print('Program kallad med mer än ett argument!')

main()
