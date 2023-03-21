import os
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

from Repositories.PersonRepository import PersonRepository

current_dir = os.getcwd()


personRepository = PersonRepository()

# on a notre ensemble de page sur ce module pour les personnes


class PersonPage:

    def __init__(self) -> None:
        pass

    # la page par defaut
    def getHomePage(self):
        personsList = personRepository.findAll()
        return render_template('person/home.html', personsList=personsList, linkAdd=url_for('person_add_page'))

    # la page formulaire d'ajout
    def getAddPersonPage(self):
        return render_template('person/add.html')

    # la partie traitement du formulaire
    def processAddPersonPage(self):
        personRepository.insert(request.form)
        return redirect(url_for('person_home_page'))
