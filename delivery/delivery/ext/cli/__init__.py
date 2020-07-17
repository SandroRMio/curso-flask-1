import click
from delivery.ext.db import db
from delivery.ext.site import models


def init_app(app):

    @app.cli.command()
    def create_db():
        """comando inicializa o BD """
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """adiciona um novo usuario"""
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f" Usuário {email} criado com sucesso  !!!")

    @app.cli.command()
    def listar_pedidos():
        click.echo("lista dos pedidos")

    @app.cli.command()
    def listar_usuarios():
        click.echo("lista dos usuarios")
