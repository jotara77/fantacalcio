import json
from calciatore import Calciatore
from squadra import Squadra
from excel import Excel
import numpy as np
import os

f = open("dataset/fantacalcio.json","r")
data:dict = json.load(f)

# Parsing dei calciatori.
calciatori:list[Calciatore] = []
for calciatore in data.values():
    parsato = Calciatore.from_json(elem = calciatore)
    calciatori.append(parsato)

squadre:list[str] = []
for cal in calciatori:
    if cal.squadra not in squadre:
        squadre.append(cal.squadra) 

foglio = Excel(calciatori=calciatori)

stagioni =["s_23_24", "s_22_23", "s_21_22","s_20_21","s_19_20","s_18_19"]
foglio.scrivi_statistiche("s_23_24")
#Salvataggio del file 
foglio.save_to_file("test.xls")
lista_calciatori = []


for elem in data.values():
    c = Calciatore.from_json(elem)
    lista_calciatori.append(c)



#Creazione del grafico 
for squadra in squadre:
    sq:Squadra = Squadra.from_lista_calciatori(squadra,lista_calciatori,stagioni)
    sq.grafico_squadra("grafico.png")




#crea cartella per salvare i grafici
os.makedirs("grafici", exist_ok=True)

# Crea grafico per ogni calciatore
for calciatore in lista_calciatori:
    if len(calciatore.media_voti) > 0:  # solo se ha dati
         percorso = f"grafici/{calciatore.nome}.png"
         calciatore.crea_grafico_voti(percorso)


#Creazione dei fogli Excel 
excel = Excel(calciatori)

excel.crea_fogli_per_stagioni(stagioni)
excel.scrivi_statistiche(stagioni)
excel.save_to_file("real.xlsx")
f.close()



#Creazioone del grafico per un determinato giocatore in un determinato anno attraverso i seguenti dati(voti, gol fatti, minuti di entrata e minuti di uscita) nelle varie giocate
calciatori[89].stats_player_grafico("s_19_20")
