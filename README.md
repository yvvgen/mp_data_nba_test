# MP DATA : Test Technique

Ce repo contient le code utilisé pour répondre au test technique pour MP DATA.

Il est structuré comme tel :

- `data` : contient les données et métadonnées utilisées
- `code` : contient le code utilisé pour répondre aux questions
- `document` : contient le sujet du test
- `models` : contient les modèles utilisés pour la prédiction
- `outputs` : contient le notebook de modélisation en format html

Dans la racine du projet se trouvent plusieurs fichier :

- `poetry.lock` et `pyproject.toml` : fichiers de configuration de l'environnement virtuel python
- `prediction.py` : l'API pour la prédiction
- `Dockerfile` : un container pour lancer l'application de prédiction

## Ajout de réponses aux questions :

### Question 1 :

Pour travailler sur ce jeu de données j'ai fait une exploration rapide des données et quelques tests de modélisation.

Après avoir essayé de travailler directement la données (pour la décorréler par exemple) je n'ai pas vu d'impact significatif sur les résultats. J'ai donc décidé de travailler directement sur les données brutes.

Je tiens à préciser que je ne pense pas que cela soit une bonne pratique de travailler directement sur les données brutes. Dans la pratique (i.e. dans des situations professionnelles) j'ai toujours observé qu'un raffinement des données, de l'extraction de features ou encore de sélection était un facteur clé de la performance des modèles (même si toutes les transformations de données ne sont pas bénéfiques bien sûr).

### Question 2 :

Pour faire l'API pour chercher les résultats du modèle, j'ai choisi l'approche d'un container. Elle me semble être le plus proche de ce qui pourrait être mis en production.

1. Pour faire fonctionner l'API, il faut se placer dans la racine du projet et lancer la commande suivante :

```bash
docker build -t mp_data_test .
```

Cette commande va construire une image docker avec toutes les dépendances nécessaires au calcul de la prédiction. La première fois cela peut prendre du temps (notamment parce que l'environnement python est commun avec celui d'exploration de la données, il contient donc beaucoup de paquets inutiles pour l'inférence).

2. Une fois l'image construite, il faut la lancer avec la commande suivante :

```bash
docker run -it -p 1717:1717 mp_data_test:latest
```

Cette commande va lancer le container et exposer le port 1717 pour faire des requêtes dessus.

3. Pour faire une requête, il faut utiliser un client HTTP (comme curl ou postman) et envoyer une requête POST sur l'url `http://localhost:1717/predict` avec un body contenant les données au format json. Par exemple :

```bash
curl -X POST -H "Content-Type: application/json" -d @./data/test_data.json http://localhost:1717/predict
```

4. J'ai choisi de faire un petit script `inference.py` pour faire des requêtes sur l'API. Il faut lancer la commande suivante :

```bash
cd code && poetry run python inference.py
```

(attention à bien se placer dans `code` pour respecter l'arborescence).