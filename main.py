#importo tutti i file e tutti i pacchetti scaricati
import json
from calciatore import Calciatore
from squadra import Squadra
from excel import Excel
import numpy as np
import os

# Apertura del file json
f = open("dataset/fantacalcio.json","r")
data:dict = json.load(f)
f.close()

# Parsing dei calciatori
calciatori:list[Calciatore] = []
for calciatore in data.values():
    parsato = Calciatore.from_json(elem = calciatore)
    calciatori.append(parsato)


#crea lista stagioni
stagioni:list[str]= []
for calciatore in calciatori:
    for stagione in calciatore.stagioni:
        if stagione not in stagioni:
            stagioni.append(stagione)

#Punto1: crea file excel
foglio = Excel(calciatori=calciatori)

#inserisce le statistiche nel foglio Excel
foglio.crea_fogli_per_stagioni(stagioni)
foglio.scrivi_statistiche(stagioni)
foglio.save_to_file("results.xls")

exit()

#Punto3:
#crea una lista di squadre a partire dalla lista di calciatori
squadre:list[str] = []
for cal in calciatori:
    if cal.squadra not in squadre:
        squadre.append(cal.squadra) 

#Creazione del grafico che rappresenta l'andamento della squadra nelle diverse stagioni
for squadra in squadre:
    sq:Squadra = Squadra.from_lista_calciatori(squadra,calciatori, stagioni)
    sq.grafico_squadra(f"grafici/squadre/{sq.nome}.jpg")

#crea cartella per salvare i grafici
os.makedirs("grafici", exist_ok=True)

# Punto 2:Creazione grafico per ogni calciatore per mv e fmv
for calciatore in calciatori:
    if len(calciatore.media_voti) > 0:  # solo se ha dati
        calciatore.crea_grafico_voti(f"grafici/voti/{calciatore.nome}.jpg")  
        #Punto 4: Creazione del grafico per un determinato giocatore in un determinato anno attraverso i seguenti dati(voti, gol fatti, minuti di entrata e minuti di uscita) nelle varie giocate
        for stagione in calciatore.stagioni:
            calciatore.stats_player_grafico(stagione,f"grafici/stats/{calciatore.nome}_{stagione}.jpg")
