from calciatore import Calciatore
import pandas as pd
import openpyxl


class Excel:
    def __init__(self, calciatori:list[Calciatore]):
        self.calciatori: list[Calciatore] = calciatori
        self.wb = openpyxl.Workbook()   
    
    
    def calciatori_attivi(self, stagione)->list[Calciatore]:
        lista_calciatori=[]
        for calciatore in self.calciatori:
            if calciatore.attivo(stagione):
                lista_calciatori.append(calciatore)
        return lista_calciatori
    
    def crea_foglio_excel(self, calciatori:list[Calciatore], anno:str):
        for calciatore in calciatori:
            if calciatore.attivo(anno):
                self.wb.create_sheet

    def scrivi_statistiche(self, stagione):
        active = self.wb.active
        

    def crea_fogli_per_stagioni(self, stagioni:list[str]):    
        for stagione in stagioni:
            sheet=self.wb.create_sheet(stagione)
            headers= ["Nome", "Media_voti", "MediaFanta", "Squadra", "Ruolo"]
            for col, header in enumerate(headers, start=1):
                sheet.cell(row=1, column=col).value = header
            sheet.freeze_panes = "A2"
            riga = 2
            for calciatore in self.calciatori:
                print(calciatore)
                print(stagione)
                print(stagione==calciatore.stagione)
                if calciatore.attivo(stagione):
                    print("cio")
                    sheet.cell(row=riga, column=1).value = calciatore.nome
                    sheet.cell(row=riga, column=2).value = calciatore.media_voti[stagione]
                    sheet.cell(row=riga, column=3).value = calciatore.media_voti_fanta[stagione]
                    sheet.cell(row=riga, column=4).value = calciatore.squadra
                    riga += 1
        return self.wb.save









    #active.append(calciatori)

    def save_to_file(self,file_path:str):
     self.wb.save(file_path)

    