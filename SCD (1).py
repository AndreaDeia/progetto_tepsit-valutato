import socket
import mysql.connector
import socket as sock
import convertitore as C
import threading as t

#server

def db_leggi():
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="andreamario_deiana",
        password="deiana1234",
        database="5ATepsit",
        port=3306,
        )
    cur = conn.cursor()
    query = "SELECT * FROM dipendenti_deiana_andrea_mario"
    cur.execute(query)
    dati = cur.fetchall()
    print(dati)
    return dati
#-----------------------------------------------------------------------------------------------------------------------
def db_elimina(i):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="andreamario_deiana",
        password="deiana1234",
        database="5ATepsit",
        port=3306,
        )
    cur = conn.cursor()
    query = f"DELETE FROM `dipendenti_deiana_andrea_mario` WHERE id={i} "
    cur.execute(query)
    conn.commit()
#-----------------------------------------------------------------------------------------------------------------------
def db_inserisci(parametri):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="andreamario_deiana",
        password="deiana1234",
        database="5ATepsit",
        port=3306,
        )
    clausole = "("
    for key in parametri:
        clausole += f"{key},"
    clausole = clausole[:-1]
    clausole += ") VALUES ("
    for val in parametri.values():
        clausole += f"'{val}',"
    clausole = clausole[:-1]
    clausole += ")"
    cur = conn.cursor()
    query = f"INSERT INTO dipendenti_deiana_andrea_mario {clausole}"
    print(query)
    cur.execute(query)
    conn.commit()
#-----------------------------------------------------------------------------------------------------------------------
def db_modifica(parametri):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="andreamario_deiana",
        password="deiana1234",
        database="5ATepsit",
        port=3306,
        )
    #UPDATE `dipendenti_deiana_andrea_mario` SET
    #`id`=[value-1],`nome`=[value-2],`cognome`=[value-3],`posizione_lavorativa`=[value-4],`settore_di_lavoro`=[value-5],`turno`=[value-6],`data_di_assunzione`=[value-7] WHERE 1
    clausole = ""
    for key, value in parametri.items():
        clausole += f"{key} = '{value}' "
    cur = conn.cursor()
    query = f"UPDATE `dipendenti_deiana_andrea_mario` SET {clausole} WHERE 1"
    print(query)
    cur.execute(query)
    conn.commit()
#-----------------------------------------------------------------------------------------------------------------------
def db_leggi1():
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="andreamario_deiana",
        password="deiana1234",
        database="5ATepsit",
        port=3306,
        )
    cur = conn.cursor()
    query = "SELECT * FROM zone_di_lavoro_deiana_andrea_mario"
    cur.execute(query)
    dati = cur.fetchall()
    print(dati)
    return dati
#-----------------------------------------------------------------------------------------------------------------------
def db_elimina1(i):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="andreamario_deiana",
        password="deiana1234",
        database="5ATepsit",
        port=3306,
        )
    cur = conn.cursor()
    query = f"DELETE FROM `zone_di_lavoro_deiana_andrea_mario` WHERE id={i} "
    cur.execute(query)
    conn.commit()
#-----------------------------------------------------------------------------------------------------------------------
def db_inserisci1(parametri):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="andreamario_deiana",
        password="deiana1234",
        database="5ATepsit",
        port=3306,
        )
    clausole = "("
    for key in parametri:
        clausole += f"{key},"
    clausole = clausole[:-1]
    clausole += ") VALUES ("
    for val in parametri.values():
        clausole += f"'{val}',"
    clausole = clausole[:-1]
    clausole += ")"
    cur = conn.cursor()
    query = f"INSERT INTO zone_di_lavoro_deiana_andrea_mario {clausole}"
    print(query)
    cur.execute(query)
    conn.commit()
#-----------------------------------------------------------------------------------------------------------------------
def db_modifica1(parametri):
    conn = mysql.connector.connect(
        host="10.10.0.10",
        user="andreamario_deiana",
        password="deiana1234",
        database="5ATepsit",
        port=3306,
        )
    #UPDATE `dipendenti_deiana_andrea_mario` SET
    #`id`=[value-1],`nome`=[value-2],`cognome`=[value-3],`posizione_lavorativa`=[value-4],`settore_di_lavoro`=[value-5],`turno`=[value-6],`data_di_assunzione`=[value-7] WHERE 1
    clausole = ""
    for key, value in parametri.items():
        clausole += f"{key} = '{value}' "
    cur = conn.cursor()
    query = f"UPDATE `zone_di_lavoro_deiana_andrea_mario` SET {clausole} WHERE 1"
    print(query)
    cur.execute(query)
    conn.commit()
#-----------------------------------------------------------------------------------------------------------------------
def comm_tabella (conn,data):
     while True:
         conn.send("Benvenuto utente, scegli quale tabella usare : \n1- dipendenti_deiana_andrea_mario \n2- zone_di_lavoro_deiana_andrea_mario")
         data = conn.recv(1024)
         if data.decode() == "1" :
             conn.send("cosa vuole fare con la sua tabella ? : \n C-Create; \n R-Read; \n U-Update; \n D-Delete.".encode())
             data = conn.recv(1024)
    # -----------------------------------------------------------------------------------------
             if data.decode() == "C" :
                p = conn.recv(1024)
                parametri = C.bytes_to_dict(p)
                db_inserisci(parametri)
                conn.send("elemento aggiunto .".encode())
    # -----------------------------------------------------------------------------------------
             if data.decode() == "R":
                 lista = list(db_leggi1())
                 conn.send(C.list_to_bytes(lista))
    # -------------------------------------------------------------------------------------------
             if data.decode() == "U":
                 p = conn.recv(1024)
                 parametri = C.bytes_to_dict(p)
                 db_modifica(parametri)
                 conn.send("elemento modificato .".encode())
    # -------------------------------------------------------------------------------------------
             if data.decode() == "D":
                 conn.send("inserisci l'operaio da eliminare [inserisci l'id]".encode())
                 i = conn.recv(1024)
                 db_elimina1(i.decode())
                 conn.send("è stato eliminato l'operaio".encode())
         if data.decode() == "2":
             conn.send(
                 "cosa vuole fare con la sua tabella ? : \n C-Create; \n R-Read; \n U-Update; \n D-Delete.".encode())
             data = conn.recv(1024)
             # -----------------------------------------------------------------------------------------
             if data.decode() == "C":
                 p = conn.recv(1024)
                 parametri = C.bytes_to_dict(p)
                 db_inserisci1(parametri)
                 conn.send("elemento aggiunto .".encode())
             # -----------------------------------------------------------------------------------------
             if data.decode() == "R":
                 lista = list(db_leggi1())
                 conn.send(C.list_to_bytes(lista))
             # -------------------------------------------------------------------------------------------
             if data.decode() == "U":
                 p = conn.recv(1024)
                 parametri = C.bytes_to_dict(p)
                 db_modifica1(parametri)
                 conn.send("elemento modificato .".encode())
             # -------------------------------------------------------------------------------------------
             if data.decode() == "D":
                 conn.send("inserisci l'operaio da eliminare [inserisci l'id]".encode())
                 i = conn.recv(1024)
                 db_elimina1(i.decode())
                 conn.send("è stato eliminato l'operaio".encode())
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__" :
    Lock = t.Lock()
    HOST = 'localhost'                  # Nome simbolico che rappresenta il nodo locale
    PORT = 50016                        # Porta non privilegiata arbitraria
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    thread = []
    lista_connessioni = []
    i = 0
    TRY = 0
    while TRY < 2 :
        lista_connessioni.append(s.accept())
        data = conn.recv(1024)
        if data.decode() == "topogigio" :
            conn.send("password accettata, premere invio. \n".encode())
            th = t.Thread(target=comm_tabella(lista_connessioni[i],data),args=(lista_connessioni[i],data))
        else :
            TRY = TRY + 1
            conn.send("inserisci di nuovo la password :".encode())
    conn.close()
    #http://10.10.0.10/phpmyadmin