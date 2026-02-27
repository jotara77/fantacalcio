from calciatore import Calciatore

class Excel:
    def __init__(self, calciatori:list[Calciatore]):
        self.calciatori: list[Calciatore] = calciatori
    
    
    def calciatori_attivi(self, stagione)->list[Calciatore]:
        lista=[]
        for calciatore in self.calciatori:
            if calciatore.attivo(stagione):
                lista.append(calciatore)
        return lista
    
    def 

        