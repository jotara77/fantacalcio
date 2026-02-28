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
foglio.scrivi_statistiche("s_23_24")
foglio.save_to_file("test.xls")

f.close()

