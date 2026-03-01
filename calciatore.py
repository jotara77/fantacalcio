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
    
    

    
    