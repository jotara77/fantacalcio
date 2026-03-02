from calciatore import Calciatore
import matplotlib.pyplot as plt
import numpy as np

class Squadra:
    def __init__(self, nome: str, calciatori:list[Calciatore],stagioni:list[str]):
        self.nome:str = nome
        self.calciatori:list[Calciatore] = calciatori  # lista di oggetti Calciatore
        self.stagioni:list[str] = stagioni

    def from_lista_calciatori(nome:str,calciatori:list[Calciatore],stagioni: list[str])->Squadra:
        lista_membri = [
            cal
            for cal in calciatori
            if cal.squadra == nome
        ]
        a = Squadra(nome,lista_membri,stagioni)
        return Squadra(nome,lista_membri,stagioni)

        
    def andamento_media_squadra_per_stagione(self,stagione):
        media_voti_calciatore_squadra = [ # costrutto one line per inizializzare
            cal.media_voti[stagione] # metti questo in lista
            for cal in self.calciatori # dalla lista dei calciatori
            if cal.media_voti.get(stagione) != None # se la media voti esiste
        ]
        if len(media_voti_calciatore_squadra) == 0:
            return None
        return sum(media_voti_calciatore_squadra) / len(media_voti_calciatore_squadra)
    
    def andamento_media_squadra(self)->list[float]:
        return [
            self.andamento_media_squadra_per_stagione(stagione)
            for stagione in self.stagioni
        ]
        
    def grafico_squadra(self,path:str):
        x_stagioni = self.stagioni
        y_medie = self.andamento_media_squadra()
        plt.plot(x_stagioni, y_medie,
             marker="o",
             markersize=8,
             label="Media Voti")

        plt.xlabel("stagione")
        plt.ylabel("media voti dei calciatori della squadra")
        plt.title("Andamento media dei voti dei calciatori della squadra: " +self.nome)
        plt.show()
        return 

        
    

