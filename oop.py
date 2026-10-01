#Definizione della classe studente
class Studente:
    #Attributi
    matr =0
    nome=""
    cognome=""

    #Costruttore, funzioni standard per iniz.l'oggetto
    def __init__(self,matr,nome,cognome):
        self.matr = matr
        self.nome = nome
        self.cognome = cognome

    #Altre funzioni
    def prenota_esame(self):
        ...


#Creo un oggetto/istanza della classe Studente
s= Studente(123456, "Mario","Rossi") #Creo uno studente e inizializzandolo
            #Python chiama la funzione __init__()
print(f"{s.matr} - {s.nome} - {s.cognome}")

s.prenota_esame() #Posso invocare su QUELLO studente Mario Rossi la funzione che serve
#DATI E OP. SUI DATI SONO INCAPUSULATE NELL'OGGETTO

#Il file è un'oggetto

#Collezione di studenti
lista_studenti=[]
lista_studenti.append(s)
lista_studenti.append(Studente(67890, "Gianni","Verdi"))

n=len(lista_studenti)
print(n)

for studenti in lista_studenti:
    print(studenti.matr,studenti.nome,studenti.cognome)





