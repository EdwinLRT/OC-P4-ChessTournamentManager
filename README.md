

# Chess Tournament Manager
## Logiciel de gestion de tournois d'échecs hors-ligne
#### Développement d'un logiciel de gestion de tournois dans le cadres du quatrième projet de la formation de développeur d'applications Python d'Openclassrooms. 

## Initialisation du projet : 

#### Windows : 

###### Copier le repo : 
```
git clone https://github.com/EdwinLRT/OC-P4-ChessTournamentManager
```
######  Créer un environement de travail virtuel : 
```
cd OC-P4-ChessTournamentManager
python -m venv env 
~env\scripts\activate
```

######  Lancer le programme  : 
```
python main.py
```


#### MacOS : 

###### Copier le repo : 
```
git clone https://github.com/EdwinLRT/OC-P4-ChessTournamentManager
```
######  Créer un environement de travail virtuel : 
```
cd OC-P4-ChessTournamentManager
python3 -m venv env 
pip install -r requirements.txt
```
######  Lancer le programme  : 
```
python3 main.py
```

## Création d'un rapport Flake8 :
#### Flake8 est un des outils mis à disposition par la communauté pour aider à valider son code Python au regard de la PEP 8.


Dernier rapport Flake8 généré : 
![Dernier rapport Flake8 - 0 erreurs](/images/flake8-rapport-01-05-23.png "Dernier rapport Flake8")

#### Pour générer un nouveau rapport : 

######  Flake8 a été installé via le fichier requirements.txt lors de l'initialisation du projet.
###### Il suffit d'entrer la commande : 
```
flake8 --format=html --htmldir=flake8_report
```
