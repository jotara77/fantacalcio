from calciatore import Calciatore
import pandas as pd
import openpyxl


class Excel:
    def __init__(self, calciatori:list[Calciatore]):
        self.calciatori: list[Calciatore] = calciatori
        self.wb = openpyxl.Workbook()   
    
    
    def calciatori_attivi(self, stagione)->list[Calciatore]:
        lista=[]
        for calciatore in self.calciatori:
            if calciatore.attivo(stagione):
                lista.append(calciatore)
        return lista
    
    def crea_foglio_excel(self, calciatori:list[Calciatore], anno:str):
        for calciatore in calciatori:
            if calciatore.attivo(anno):
                self.wb.create_sheet(anno)

    def scrivi_statistiche(self, stagione):
        active = self.wb.active
        active["A1"] = "Nome"
        active["B1"] = "Media Voti"
        active["C1"] = "Media Voti Fanta"
        active["D1"] = "Squadra"
        active["E1"] = "Ruolo"
        active["F1"] = ""
        calciatori = []
        # for calciatore in self.calciatori_attivi(stagione):
        #     calciatori.append(f"{calciatore}")
        # active.append(calciatori)

    def save_to_file(self,file_path:str):
        self.wb.save(file_path)

            