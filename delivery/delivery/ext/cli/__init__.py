import click
from delivery.ext.db import db


def init_app(app):

    @app.cli.command()
    def create_db():
        """comando inicializa o BD """
        db.create_all()

    @app.cli.command()
    def listar_pedidos():
        click.echo("lista dos pedidos")

    @app.cli.command()
    def listar_usuarios():
        click.echo("lista dos usuarios")
