import click

from delivery.ext.auth.models import User
from delivery.ext.auth.controller import create_user


# TODO: mover para o controller
def list_users():
    users = User.query.all()
    click.echo(f"lista de usuarios {users}")


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """adiciona novo usuario"""
    # TODO: criiar um try/except caso ja exista o user

    create_user(email=email, password=passwd, admin=admin)

    click.echo(f"Usuário {email} criado com sucesso!")


def listar_usuarios():
    users = User.query.all()
    click.echo("lista dos usuarios {users}")
