from flask import render_template
from flask import Blueprint
from flask import current_app
from delivery.ext.auth.form import UserForm

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    print("entrei na funcao main")
    current_app.logger.debug("Entrei na funcao main")
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/cadastro")
def signup():
    form = UserForm()
    return render_template("restaurants.html", form=form)

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")
