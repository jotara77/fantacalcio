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
# c1 = Calciatore("mario","2018_2019",{"2018_2019":"12"},{"2018_2019":"152"}, "Lazio")
# c2 = Calciatore("giorgio", "2019_2020",{"2019_2020":"8"},{"2019_2020":"125"}, "Juventus")
# c3 = Calciatore("sara", "2024_2025", {"2024_2025":"6"},{"2024_2025":"142"}, "milan")

excel = Excel(calciatori)

stagioni =["s_23_24", "s_22_23", "s_21_22","s_20_21","s_19_20","s_18_19"]

excel.crea_fogli_per_stagioni(stagioni)
excel.scrivi_statistiche(stagioni)
excel.save_to_file("real.xlsx")
f.close()

