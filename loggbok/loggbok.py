fileHandle = "log.txt"

while True:
    val = input('[1] Läs logg\n[2] Skriv logg\n[3] Rensa logg\n[4] Avsluta\nVal:')

    if val =        §§"1":
        print('Alla loggar')


        with open(fileHandle, 'r', encoding='utf-8') as logfile:
            for linre in logfile:
                log = line.split('')


    elif val = "2":
        print('Skriv en logg')

    elif val = "3":
        print('Rensa')

    elif val = "4":
        print('Hejdå')
        break

    else:
        print('Felaktigt val')