class Calciatore:
    def __init__(self, stagione, media_voti, media_voti_fanta, squadra,):
        self.stagione=  stagione
        self.media_voti= media_voti
        self.media_voti_fanta= media_voti_fanta
        self.squadra= squadra

    def attivo(self, stagione):
        return self.stagione == stagione
