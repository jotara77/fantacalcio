import json
from calciatore import Calciatore
from excel import Excel

f = open("dataset/fantacalcio.json","r")
data:dict = json.load(f)

# Parsing dei calciatori.
calciatori = []
for calciatore in data.values():
    parsato = Calciatore.from_json(elem=calciatore)
    calciatori.append(parsato)


foglio = Excel(calciatori=calciatori)
#foglio.scrivi_statistiche("s_23_24")
foglio.save_to_file("test.xls")
c1 = Calciatore("2018_2019", "4","12", "Lazio")
c2 = Calciatore("2019_2020","7","15", "Juventus")

excel = Excel([c1, c2])

excel.crea_fogli_per_stagioni(["2018_2019", "2019_2020"])
excel.salva("test.xlsx")
f.close()

