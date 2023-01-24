from flask import Flask, render_template, request, redirect, url_for
from services.marvelk import herois, get_convocados
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = b'H\xa2\x8c\xf8\x81\xe8\xa3\x16!Pu\x89;\x19\x85\xe1'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vigadores.sqlite3"

db = SQLAlchemy(app)


class Convocados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer)
    type = db.Column(db.String(50))

    def __init__(self, hero_id, type):
        self.hero_id = hero_id
        self.type = type


with app.app_context():
    db.create_all()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("types"):
            hero_id = request.form.get("id")
            type = request.form.get("types")
            convocados = Convocados(hero_id, type)
            db.session.add(convocados)
            db.session.commit()
            return redirect((url_for('convocados')))

    search = request.args.get('search')
    lista_herois = herois(search if search else '')
    return render_template('index.html', lista_herois=lista_herois)


# @app.route('/convocados', methods=["GET", "POST"], defaults={"page": 1})
@app.route('/convocados', methods=["GET"])
def convocados():
    # Lista os Heris selecionados como vingadores
    # page = request.args.get('page', 1, type=int)
    # per_page = 4
    herois_convocados = Convocados.query.all()
    # herois_convocados = Convocados.query.paginate(page=page, per_page=per_page)
    convocados_detalhes = get_convocados(herois_convocados)
    return render_template('convocados.html', lista_herois=convocados_detalhes)


@app.route('/remove_heroi/<int:id>')
def remove_heroi(id):
    # Remove o heroi da lista
    hero = Convocados.query.get(id)
    db.session.delete(hero)
    db.session.commit()
    return redirect(url_for('convocados'))


if __name__ == "__main__":
    app.run(debug=True)
