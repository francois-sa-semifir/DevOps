# DevOps - Récapitultif des installations et de la configuration de l'environnement

## Installation de Python

Récupération de la dernière version stable sur le site officiel
<https://www.python.org/downloads/windows/>

Vérification de la version

```bash
python --version
```

## Installation de Flask

```bash
pip install flask
```

Vérification de la version

```bash
flask --version
```

## Démarrer un serveur FLASK

```bash
python app.py
```

## Installer MongoDB via Docker

```bash
docker pull mongo
```

```bash
docker run --name test-mongo -d --env MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=test1234 -p 27017:27017 mongo:latest
```

## Se connecter à Mongo via Compass

mongodb://root:test1234@localhost:27017/

+ Username et MDP

## Installer pymongo (connecteur Mongo/Python)

```bash
pip install pymongo
```

## Installer pytest (connecteur Mongo/Python)

```bash
pip install pytest
```

