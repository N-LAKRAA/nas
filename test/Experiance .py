import csv
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import statit_py
# or: requests.get(url).content

# resp = urlopen("http://www.test.com/file.zip")
# myzip = ZipFile(BytesIO(resp.read()))
# for line in myzip.open(file).readlines():
#     print(line.decode('utf-8'))

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

print(my_list)
for row in my_list:
    row.pop()
    row[1] = int(row[1])


print(my_list)


statitAPI = statit_py.coreAPI('n_lakraa', '6_mExvLx')
print(statitAPI.getSerie('xr/monthly/eur/usd'))
print(statitAPI.putSerieJSON({
    'id': "insee/automobile/immatriculations_de_vehicules_neufs",
    "name" : "Immatriculations de véhicules neufs",
    "frequency" : "Y",
    "description" : "immatriculations de véhicules neufs - Ensemble - France entière ",
    "unit" : "immatriculations",
    "sources" : "Insee",
    "observations" : my_list
}))

print(my_list)
# import requests
# import csv
# res = requests.get('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')
# print(res.text)

# with requests.Session() as s:
#     download = s.get('http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv')

#     decoded_content = download.content.decode('utf-8')




# import csv
# import requests
# with requests.Session() as s:
#     s.post("https://www.insee.fr/fr/statistiques/serie/telecharger/csv/001770620?ordre=antechronologique&transposition=donneescolonne&periodeDebut=1&anneeDebut=2010&periodeFin=1&anneeFin=2023&revision=sansrevisions data=payload")
#     download = s.get('https://www.insee.fr/fr/statistiques/serie/telecharger/csv/001770620?ordre=antechronologique&transposition=donneescolonne&periodeDebut=1&anneeDebut=2010&periodeFin=1&anneeFin=2023&revision=sansrevisions')
# with requests.Session() as s:
#     download = s.get("https://www.insee.fr/fr/statistiques/serie/telecharger/csv/001770620?ordre=antechronologique&transposition=donneescolonne&periodeDebut=1&anneeDebut=2010&periodeFin=1&anneeFin=2023&revision=sansrevisions")

#     decoded_content = download.content.decode('utf-8')

#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
#         print(row)
    
# import requests
# url = "https://www.insee.fr/fr/statistiques/serie/telecharger/csv/001770620?ordre=antechronologique&transposition=donneescolonne&periodeDebut=1&anneeDebut=2010&periodeFin=1&anneeFin=2023&revision=sansrevisions"
# response = requests.get(url)
# if response.status_code == 200:
#     with open("file.zip", "wb") as file:
#         file.write(response.content)
#         print("File downloaded successfully!")
# else:
#     print("Failed to download the file.")

