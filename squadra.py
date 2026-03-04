#importazione della classe "Calciatore" dal file "calciatore.py"
from calciatore import Calciatore
#importazione dei pacchetti una volta installati 
import matplotlib.pyplot as plt
import numpy as np

class Squadra:  
    """Creazione di una classe denominata "Squadra" descrivendo il nome, la lista dei calciatori e la lista delle stagioni"""
    def __init__(self, nome: str, calciatori:list[Calciatore],stagioni:list[str]):
        self.nome:str = nome
        self.calciatori:list[Calciatore] = calciatori  # lista di oggetti Calciatore
        self.stagioni:list[str] = stagioni

    def from_lista_calciatori(nome:str,calciatori:list[Calciatore],stagioni: list[str])->Squadra:    
        #Creazione di una funzione che permette di ottenere la lista dei calciatori della stessa squadra in determinata stagione
        lista_membri = []
        for cal in calciatori:
            if cal.squadra == nome:
                lista_membri.append(cal)
        
        a = Squadra(nome,lista_membri,stagioni)
        return Squadra(nome,lista_membri,stagioni)

        
    def andamento_media_squadra_per_stagione(self,stagione):    
        # si ottiene una lista con la media dei voti dei calciatori di una determinata squdra in una determinata stagione
        media_voti_calciatore_squadra = [] 
        for cal in self.calciatori: # dalla lista dei calciatori
            if cal.media_voti.get(stagione) != None: # se la media voti esiste
                media_voti_calciatore_squadra.append(cal.media_voti[stagione]) # aggiungi alla lista "media_voti_calciatore_squadra"
        
        if len(media_voti_calciatore_squadra) == 0:
            return None
        return sum(media_voti_calciatore_squadra) / len(media_voti_calciatore_squadra)
    
    def andamento_media_squadra(self)->list[float]:
        #Restituisce una lista contenente tutti i risultati(media squadra)
        risultati = []
        for stagione in self.stagioni:
            risultati.append(self.andamento_media_squadra_per_stagione(stagione))
            
        return risultati
        
    def grafico_squadra(self,path:str):   #si ottiene grafico che rappresenta l'andamento della media dei voti dei giocatori della squadra
        x_stagioni = self.stagioni
        y_medie = self.andamento_media_squadra()
        plt.figure()
        plt.plot(x_stagioni, y_medie,
             marker="o",
             markersize=8,
             label="Media Voti")

        plt.xlabel("stagione")
        plt.ylabel("media voti dei calciatori della squadra")
        plt.title("Andamento media dei voti dei calciatori della squadra: " +self.nome)
        plt.savefig(path)
        plt.close()
        return 

        
    

