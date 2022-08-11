print("Rubrica telefonica")
elenco = dict()
while (True):
    cmd = input("Inserisci un comando (premi 'h' per l'help): ").upper()
    if (cmd == 'Q'):
        break
    elif (cmd == 'H'):
        print('q per terminare')
        print('h per l\'help')
        print('i per inserire')
        print('l per stampare tutti i nominativi')
        print('s per cercare un nome')
        print('d per eliminare un nome')
    elif (cmd == 'L'):
        chiavi = elenco.keys()
        for chiave in chiavi:
            print(f'Nominativo: {chiave} - Telefono: {elenco[chiave]}')
    elif (cmd == 'I'):
        print('Inserisci prima il nome e poi il numero di telefono.')
        while True:
            nome = input("Nome?: ").upper()
            if nome == "":
                break
            num = input("Numero?: ")
            elenco[nome] = num
            print('Vuoi inserire un altro nominativo? (premi INVIO per uscire): ')
    elif (cmd == 'S'):
        nome = input("Quale Nominativo vuoi cercare?: ").upper()
        if nome in elenco:
            tel = elenco[nome]
            print(f"tel: {tel}")
        else:
            print("Nominativo non presente!")
    elif (cmd == 'D'):
        nome = input("Quale Nominativo vuoi eliminare?: ").upper()
        if nome in elenco:
            del elenco[nome]
            print("Nominativo eliminato")
        else:  print("Nominativo non presente!")
    else:  print("Comando non previsto.")
    print("Fatto!")
