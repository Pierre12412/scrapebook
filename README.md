Assurez vous d'avoir la version 3.9.4 de Python

Pour créer un environnement virtuel, lancez la commande suivante depuis le fichier du projet : python -m venv virtualenv

Activez le ensuite avec la commande : virtualenv\Scripts\activate.bat

Puis récupérez les packages Python de requirements.txt avec la commande suivante : pip install -r requirements.txt

Enfin executez le programme en tapant dans la console : scraping.py 

Toutes les données générées par les livres sont rangés par catégorie dans le dossier ./categories sous format .csv

Toutes les images sont sauvegardées dans le dossier ./images/{catégorie}/{upc}.png sous format .png