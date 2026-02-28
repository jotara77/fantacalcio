import json
from calciatore import Calciatore
from excel import Excel

f = open("dataset/fantacalcio.json","r")
data:dict = json.load(f)

# Parsing dei calciatori.
calciatori = []
for calciatore in data.values():
    parsato = Calciatore.from_json(elem = calciatore)
    calciatori.append(parsato)


foglio = Excel(calciatori=calciatori)
#foglio.scrivi_statistiche("s_23_24")
#foglio.save_to_file("test.xls)
c1 = Calciatore("mario","2018_2019",{"2018_2019":"12"},{"2018_2019":"152"}, "Lazio")
c2 = Calciatore("giorgio", "2019_2020",{"2019_2020":"8"},{"2019_2020":"125"}, "Juventus")
c3 = Calciatore("sara", "2024_2025", {"2024_2025":"6"},{"2024_2025":"142"}, "milan")

excel = Excel([c1, c2,c3])

excel.crea_fogli_per_stagioni(["2018_2019", "2019_2020", "2024_2025"])
excel.save_to_file("test1.xlsx")
f.close()

