class Calciatore:
    def __init__(self, nome, stagione, media_voti, media_voti_fanta, squadra):
        self.nome= nome
        self.stagione=  stagione
        self.media_voti= media_voti
        self.media_voti_fanta= media_voti_fanta
        self.squadra= squadra

    def from_json(elem)->Calciatore:
        """
        Crea un oggetto Calciatore dato un elemento della lista dei calciatori del Json
        """
        stats:list = elem["stats"]
        media_voti_per_stagione={}
        media_voti_fanta_per_stagione={}
        for s in stats:
            media_voti_per_stagione[s["season"]] = s["mv"]
            media_voti_fanta_per_stagione[s["season"]] =s["fmv"]

        return Calciatore(nome= elem["name"],stagione=elem["season"], media_voti=media_voti_per_stagione, media_voti_fanta = media_voti_fanta_per_stagione, squadra=elem["team_name_short"])

    def __str__(self):
        return f"stagione: {self.stagione}, media_voti: {self.media_voti}, media_voti_fanta: {self.media_voti_fanta}, squadra: {self.squadra}"

    def attivo(self, stagione):
        return self.stagione == stagione
    
    