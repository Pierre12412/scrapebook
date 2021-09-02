Pour créer un environnement virtuel, lancez la commande suivante depuis le fichier du projet : python -m venv virtualenv

Activez le ensuite avec la commande : virtualenv\Scripts\activate.bat

Puis récupérez les packages Python de requirements.txt avec la commande suivante : pip install -r requirements.txt

Enfin executez le programme en tapant dans la console : scraping.py 

Toutes les données générées par les livres sont rangés par catégorie dans le dossier ./categories sous format .csv
Toutes les images sont sauvegardées dans le dossier ./images/{catégorie}/{upc}.png sous format .png

En lançant le programme, il va d'abord sauvegarder le premier livre de la page d'accueil (ce qui créer le dossier book avec les détails de celui-ci dedans ainsi que le dossier images de la catégorie correspondante)
Il va ensuite enregistrer tout les livres de la page (ce qui créer les dossiers catégories (qui contient les infos csv)) --> de la catégorie Travel en exemple
Puis enregistrer tout les livres du site. (images et détails par catégorie)





-exctract_infos_from_one(index,ask_csv) prend en paramètre l'index du livre sur la page actuelle et renvoit tout son détail sous forme d'un tableau de chaîne de charactère (et télécharge son image).
Le paramètre ask_csv est un booléen qui, si il est sur True, va créer un dossier books si il n'est pas créer et y mettre le détail du livre en csv sous la forme : {upc}.csv

-exctract_all_page(category) prend en paramètre la catégorie demandée (par exemple 'poetry') et extrait les données de tout les livres des pages de la catégorie demandée (et télécharge l'image de chacun)

-exctract_all_site() ne prend pas de paramètre et récupère les données de chaque livre, de chaque catégorie et télécharge chaque image. 