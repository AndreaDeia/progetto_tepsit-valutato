import socket
import convertitore as C

# client

if __name__ == "__main__":
    HOST = 'localhost'  # Il nodo remoto, qui metti il tuo indirizzo IP per provare connessione server e client dalla tua macchina alla tua macchina
    PORT = 50026  # La stessa porta usata dal server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("benvenutto,inserire la password: ")
    messaggio = input()
    s.send(messaggio.encode())
    while True:
        if messaggio == "STOP":
            s.close()
        data = s.recv(1024)
        print(data.decode())
        messaggio = input()
        s.send(messaggio.encode())
        if messaggio=="C":
            #id,nome,cognome,posizione_lavorativa,settore_di_lavoro,turno,data_di_assunzione
            nome = input("inserisci nome da inserire nei dati: ")
            cognome = input("inserisci cognome da inserire nei dati: ")
            posizione_lavorativa = input("inserisci posizione lavorativa da inserire nei dati: ")
            settore_di_lavoro = input("inserisci settore di lavoro da inserire nei dati: ")
            turno = input("inserisci turno da inserire nei dati: ")
            data_di_assunzione = input("inserisci data di assunzione da inserire nei dati [ format : AA-MM-GG ]: ")
            par = {"nome": nome, "cognome": cognome, "posizione_lavorativa":posizione_lavorativa,
                   "settore_di_lavoro": settore_di_lavoro, "turno":turno, "data_di_assunzione":data_di_assunzione}
            s.send(C.dict_to_bytes(par))
        if messaggio=="C2":
            nome_zona = input("inserisci nome_zona da inserire nei dati: ")
            numero_clienti = input("inserisci numero_clienti da inserire nei dati: ")
            id_dipendente = input("inserisci id_dipendente da inserire nei dati: ")
            orario_apertura = input("inserisci settore di lavoro da inserire nei dati: ")
            par = {"nome_zona": nome_zona, "numero_clienti": numero_clienti, "id_dipendente":id_dipendente,
                   "orario_apertura": orario_apertura}
            s.send(C.dict_to_bytes(par))
        if messaggio=='R':
            data = s.recv(1024)
            dati = C.bytes_to_list(data)
            print(dati)
        if messaggio=="U":
            #id,nome,cognome,posizione_lavorativa,settore_di_lavoro,turno,data_di_assunzione
            id = input("inserisci l'id da modificare: ")
            nome = input("inserisci il nome da modificare: ")
            cognome = input("inserisci il cognome da modificare: ")
            posizione_lavorativa = input("inserisci la posizione lavorativa da modificare: ")
            settore_di_lavoro = input("inserisci il settore di lavoro da modificare: ")
            turno = input("inserisci il turno da modificare: ")
            data_di_assunzione = input("inserisci la data di assunzione da modificare [ format : AA-MM-GG ]: ")
            par = {"id" : id , "nome": nome, "cognome": cognome, "posizione_lavorativa":posizione_lavorativa,
                   "settore_di_lavoro": settore_di_lavoro, "turno":turno, "data_di_assunzione":data_di_assunzione}
            s.send(C.dict_to_bytes(par))
            ID = input("inserisci quale elemento bisogna modificare : ")
            s.send(ID.encode())