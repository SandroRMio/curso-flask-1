import click
from delivery.ext.db import db
from delivery.ext.site import models


def init_app(app):

    @app.cli.command()
    def create_db():
        """comando inicializa o BD """
        db.create_all()

    @app.cli.command()
    @click.option("--name", "-n")
    def add_category(name):
        """adiciona um nova categoria..."""
        category = models.Category(
            name=name
        )
        db.session.add(category)
        db.session.commit()

        click.echo(f" Categoria {name} criado com sucesso  !!!")

    # flask add-user --email=sandrormio@com --passw=222

    @app.cli.command()
    @click.option("--zip", "-z")
    @click.option("--country", "-c")
    @click.option("--address", "-a")
    @click.option("--user_id", "-u")
    def add_address(zip, country, address, user_id):
        """adiciona um novo endereço"""
        address = models.Address(
            zip=zip,
            country=country,
            address=address,
            user_id=user_id
        )
        db.session.add(address)
        db.session.commit()

        click.echo(f" Endereço {address} criado com sucesso  !!!")

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
