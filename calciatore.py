import matplotlib.pyplot as plt 
import numpy as np
import matplotlib as mp

class Calciatore:
    def __init__(self, nome, ruolo, stagione, media_voti, media_voti_fanta, squadra):
        self.nome: str = nome
        self.ruolo: str = ruolo
        self.stagione: list =  stagione
        self.media_voti: dict = media_voti
        self.media_voti_fanta: dict = media_voti_fanta
        self.squadra: str = squadra
        
        

    def from_json(elem)->Calciatore:
        """
        Crea un oggetto Calciatore dato un elemento della lista dei calciatori del Json
        """
        stats:list = elem["stats"]
        media_voti_per_stagione={}
        media_voti_fanta_per_stagione={}
        for s in stats:
            if s["mv"] != None and s["fmv"] != None:  #non salvo mv e fmv per la stagione SE NON esisitono
                media_voti_per_stagione[s["season"]] = s["mv"]
                media_voti_fanta_per_stagione[s["season"]] = s["fmv"]

        return Calciatore(nome= elem["name"],ruolo= elem["role"],stagione=elem["season"], media_voti=media_voti_per_stagione, media_voti_fanta = media_voti_fanta_per_stagione, squadra=elem["team_name_short"])

    def __str__(self):
        return f"stagione: {self.stagione}, media_voti: {self.media_voti}, media_voti_fanta: {self.media_voti_fanta}, squadra: {self.squadra}"

    def attivo(self, stagione):
        """
        controlla che la mv e fmv della stagione attiva esistano per questo calciatore
       e che siano diverse da zero 
        """
        return self.media_voti.get(stagione, 0) != 0 and self.media_voti_fanta.get(stagione, 0) != 0
    
    def crea_grafico_voti(self, path):
        """
        Crea il grafico della media dei voti di questo calciatore e salva il grafico in un immagine a <path>
        """
        x_stagioni = np.array(list(self.media_voti.keys()))
        y_valori_mv = np.array(list(self.media_voti.values()))
        x_stagioni_fmv = np.array(list(self.media_voti_fanta.keys()))
        y_valori_fmv = np.array(list(self.media_voti_fanta.values()))
        plt.plot(x_stagioni, y_valori_mv,
             marker="o",
             markersize=8,
             label="Media Voto")

        plt.plot(x_stagioni_fmv, y_valori_fmv,
             marker="s",
             markersize=8,
             label="Media Voto Fanta")

        plt.xlabel("stagione")
        plt.ylabel("media voto e media voto fanta")
        plt.title("Andamento media voto e media voto fanta del calciatore: " +self.nome)
        plt.show()
        return 

    def stats_player_from_json(self):


        

    
