'''Importation de Flask et des Blueprints depuis les modules des routes'''
from flask import Flask
from routes.main_routes import main_bp

'''Création d'une application Flask'''
app = Flask(__name__)

'''Enregistrement des blueprints dans l'application Flask'''
app.register_blueprint(main_bp)

'''Exécution de l'application si elle est directement exécutée'''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

"""
Flask est importé depuis le module flask. 
C'est la classe principale qui représente l'application Flask.

Les blueprints (main_bp et admin_bp) sont importés depuis les modules des routes.

Une instance de l'application Flask est créée avec Flask(__name__). __name__ représente le nom du module actuel.

Les blueprints sont enregistrés dans l'application Flask avec app.register_blueprint().
Cela monte les routes définies dans chaque blueprint dans l'application principale.

"""
