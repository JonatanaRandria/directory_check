import requests
import time

checked=[]



with open("dir_list.txt", "r") as fichier:
    time.sleep(2)  # Exemple de code, à remplacer par votre propre code

# Enregistrer le temps de début
    debut = time.time()
    for i in fichier:
        
        url = "http://127.0.0.1:5000/" + i.strip() 
        print('Testing : '+ i)
        response = requests.get(url)
        if response.status_code != 404:
            checked.append(url)
    print('Found the following path :')
    for g in checked:
        print(g)
