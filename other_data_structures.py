lista=[4,6]

tupla=(4,6) #la tupla, a differenza della lista, é immutabile

#Esempio di tupla
punto_nello_spazio= (4,6,-5)

#Dizionario di studenti con chiave la matricola e valore il nome/cognome
diz_studenti={"012345":"Mario Rossi","67890": "Gianni Verdi"}

#Con una lista di liste(ovvero una tabella)
lista_studenti=[["012345","Mario Rossi"],
                ["67890", "Gianni Verdi"]
                ]
#Liste separate
lista_matricole=["012345","67890"]
lista_nomi_cognomi=["Mario Rossi","Gianni Verdi"]

nuova_lista=lista_studenti #Non copia la lista
#Crea solamente un "alias", in memoria i dati non sono stati duplicati

copia_della_lista=list(nuova_lista)

