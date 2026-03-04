#installazione dei pacchetti numpy e matplotlib per la rappresentazione dei dati attraverso i grafici 
import matplotlib.pyplot as plt 
import numpy as np

class Calciatore:     #Crea una classe denominata "Calciatore" definendo i sui dati
    def __init__(self, nome, ruolo, stagione, media_voti, media_voti_fanta, squadra, gamestats):
        self.nome: str = nome
        self.ruolo: str = ruolo
        self.stagione: list =  stagione
        self.media_voti: dict = media_voti
        self.media_voti_fanta: dict = media_voti_fanta
        self.squadra: str = squadra
        self.gamestats: dict = gamestats
        
        

    def from_json(elem)->Calciatore:   #Crea un oggetto Calciatore dato un elemento della lista dei calciatori del Json
        stats:list = elem["stats"]
        media_voti_per_stagione={}
        media_voti_fanta_per_stagione={}
        gamestats = {}
        for s in stats:
            if s["mv"] != None and s["fmv"] != None:  ##non salvo mv e fmv per la stagione SE NON esisitono
                media_voti_per_stagione[s["season"]] = s["mv"]
                media_voti_fanta_per_stagione[s["season"]] = s["fmv"]
        
        
        for g in elem.get("gamestats",[]):
            gamestats[g["day"]]=g      ##creo un dizionario per ogni giornata giocata con dentro le gamestats di quella giornata
                
        return Calciatore(nome= elem["name"],ruolo= elem["role"],stagione=elem["season"], media_voti=media_voti_per_stagione, media_voti_fanta = media_voti_fanta_per_stagione, squadra=elem["team_name_short"], gamestats = gamestats)

    def __str__(self):  #Crea una funzione che restituisce i vari dati(stagione, media voti, media voti al fantacalcio e la squadra) del calciatore selezionato
        return f"stagione: {self.stagione}, media_voti: {self.media_voti}, media_voti_fanta: {self.media_voti_fanta}, squadra: {self.squadra}"

    def attivo(self, stagione):    #controlla che la mv e fmv della stagione attiva esistano per questo calciatore e che siano diverse da zero
        return self.media_voti.get(stagione, 0) != 0 and self.media_voti_fanta.get(stagione, 0) != 0
    
    def crea_grafico_voti(self, path):             # Crea il grafico della media dei voti di questo calciatore e salva il grafico in un immagine a <path>
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

    def stats_player_grafico(self, stagione):   #Questa funzione crea un grafico riguardante i dati (voti, gol fatti, minuti di entrata e minuti di uscita) di un giocatore selezionato in un determinato anno(stagione) nelle varie giornate giocate 
    
        giorni = []
        y_voto = []
        y_gol = []
        y_sub_in = []
        y_sub_out = []

        # filtro per stagione
        for g, stats in self.gamestats.items():     #attarverso questo ciclo for avviene una partizione per stagione
            if stats.get("season") == stagione:
                giorni.append(int(g))

        giorni.sort()

        for g in giorni:
            stats = self.gamestats[g]

            giorni_val = g
            voto = stats.get("vote", 0)
            gol = stats.get("gol_fatti", 0)

            sub_in = stats.get("sub_in")
            if sub_in is None:
                sub_in = 0

            sub_out = stats.get("sub_out")
            if sub_out is None:
                sub_out = 0

            giorni_val = int(g)

            y_voto.append(voto)
            y_gol.append(gol)
            y_sub_in.append(sub_in )  #/ 90) * 10)
            y_sub_out.append(sub_out)   #/ 90) * 10)

        # CREAZIONE GRAFICO
        fig, ax1 = plt.subplots()

        # Asse sinistro
        ax1.plot(giorni, y_voto, marker="o", color= "blue",label="Voto")
        ax1.plot(giorni, y_gol, marker="s", color= "green",label="Gol Fatti")
        ax1.set_xlabel("Giornata")
        ax1.set_ylabel("Voto e Gol")
        ax1.set_ylim(bottom=0)

        # Asse destro
        ax2 = ax1.twinx()
        ax2.plot(giorni, y_sub_in, marker="^", linestyle="--", color="red", label="Sub In (norm)")
        ax2.plot(giorni, y_sub_out, marker="v", linestyle="--", color= "orange", label="Sub Out (norm)")
        ax2.set_ylabel("Minuti normalizzati")
        ax2.set_ylim(bottom=0)

        # Legenda 
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2)
        #asse x
        ax1.set_xlim(left=1)

        plt.title("Statistiche di " + self.nome + " - " + stagione)
        plt.show()