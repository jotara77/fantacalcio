#importazione pacchetti una volta installati e importazione file python
from calciatore import Calciatore
import pandas as pd
import openpyxl


class Excel:
    def __init__(self, calciatori:list[Calciatore]):
        self.calciatori: list[Calciatore] = calciatori
        self.wb = openpyxl.Workbook()
        self.wb.remove(self.wb.active)  #rimuove la prima pagina vuota dell'excel
    
    
    def calciatori_attivi(self, stagione)->list[Calciatore]:
        """aggiunge alla ista i calciatori solo se sono attivi in quella stagione"""
        lista_calciatori=[]
        for calciatore in self.calciatori:
            if calciatore.attivo(stagione):
                lista_calciatori.append(calciatore)
        return lista_calciatori
    
    def crea_foglio_excel(self, calciatori:list[Calciatore], anno:str):
        """Creaziione di un foglio excel in cui ci sono i calciatori attivi in un determinato anno(stagione)"""
        for calciatore in calciatori:
            if calciatore.attivo(anno):
                self.wb.create_sheet

    def scrivi_statistiche(self, stagioni:list[str]):
        """ inserisce i dati dei calciatori nei foglio <stagioni> excel se sono attivi nella stagione"""
        for stagione in stagioni:
            sheet= self.wb[stagione] #prende il foglio dal nome stagione
            if sheet:
                headers= ["Nome", "Media_voti", "MediaFanta", "Squadra", "Ruolo"]
                for col, header in enumerate(headers, start=1):
                    sheet.cell(row=1, column=col).value = header
                sheet.freeze_panes = "A2"
                riga = 2
                for calciatore in self.calciatori:
                    if calciatore.attivo(stagione):
                        sheet.cell(row=riga, column=1).value = calciatore.nome
                        sheet.cell(row=riga, column=2).value = calciatore.media_voti[stagione]
                        sheet.cell(row=riga, column=3).value = calciatore.media_voti_fanta[stagione]
                        sheet.cell(row=riga, column=4).value = calciatore.squadra
                        sheet.cell(row=riga, column=5).value = calciatore.ruolo
                        riga += 1


    def crea_fogli_per_stagioni(self, stagioni:list[str]):    
        """Creazione fogli excel per ogni anno con i suoi calciatori attivi"""
        for stagione in stagioni:
            self.wb.create_sheet(stagione)  
        return

    def save_to_file(self,file_path:str):
        #salvataggio file excel
        self.wb.save(file_path)

    