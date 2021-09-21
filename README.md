Ce programme est utilisé pour extraire toutes les informations sur la bibliothèque en ligne : http://books.toscrape.com/

                -------------------------------------------------------------------------------
                
https://github.com/Pierre12412/scrapebook

Assurez vous d'avoir la version 3.9.4 de Python

Pour créer un environnement virtuel, lancez la commande suivante depuis répertoire : python -m venv virtualenv

Activez le ensuite avec la commande : virtualenv\Scripts\activate.bat

Puis récupérez les dépendances Python de requirements.txt avec la commande suivante : pip install -r requirements.txt

Enfin executez le programme en tapant dans la console : scraping.py 

Toutes les données générées par les livres sont rangés par catégorie dans le dossier ./categories sous format .csv

Toutes les images sont sauvegardées dans le dossier ./images/{catégorie}/{upc}.png sous format .png
