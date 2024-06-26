import csv
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import statit_py
# or: requests.get(url).content

resp = urlopen('https://www.insee.fr/fr/statistiques/serie/telecharger/csv/001770620?ordre=antechronologique&transposition=donneescolonne&periodeDebut=1&anneeDebut=2010&periodeFin=1&anneeFin=2023&revision=sansrevisions')
myzip = ZipFile(BytesIO(resp.read()))
lines = []
for line in myzip.open('valeurs_annuelles.csv').readlines():
    lines.append(line.decode('utf-8'))

cr = csv.reader(lines, delimiter=';')
my_list = list(cr)

my_list.pop(0)
my_list.pop(0)
my_list.pop(0)
my_list.pop(0)

for row in my_list:
    row.pop()
    row[1] = int(row[1])

statitAPI = statit_py.coreAPI('n_lakraa', '6_mExvLx')

print(statitAPI.putSerieJSON({
    'id': "insee/automobile/immatriculations_de_vehicules_neufs",
    "name" : "Immatriculations de véhicules neufs",
    "frequency" : "Y",
    "description" : "immatriculations de véhicules neufs - Ensemble - France entière ",
    "unit" : "immatriculations",
    "sources" : "Insee",
    "observations" : my_list
}))

