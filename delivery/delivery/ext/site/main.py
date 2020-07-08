from flask import render_template
from flask import Blueprint
from flask import current_app

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    current_app.logger.debug("tretpreutertiert")
    return render_template("index.html")


@bp.route("/conheca")
def about():
    return render_template("about.html")


@bp.route("/restauracao")
def restaurants():
    return render_template("restaurants.html")
