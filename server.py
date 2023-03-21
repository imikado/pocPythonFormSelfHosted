from flask import Flask

from Pages.PersonPage import PersonPage

app = Flask(__name__, template_folder='Pages/templates')

personPage = PersonPage()

# ici on definit les pages avec le chemin et le verb http: GET pour la consultation, POST lorsque l'on soumet un formulaire


@app.route("/", methods=["GET"])
def person_home_page():
    return personPage.getHomePage()

# par exemple ici on affiche le formulaire


@app.route("/add", methods=["GET"])
def person_add_page():
    return personPage.getAddPersonPage()

# ici on traite le fait d'avoir soumis le formulaire


@app.route("/add", methods=["POST"])
def person_process_add_page():
    return personPage.processAddPersonPage()
