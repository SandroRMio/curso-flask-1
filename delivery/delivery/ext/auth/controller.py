import os
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask import current_app as app
from delivery.ext.auth.models import User

from delivery.ext.db import db


ALG = "pbkdf2:sha256"


def create_user(email: str, password: str, admin: bool = False) -> User:
    user = User(
        email=email,
        passwd=generate_password_hash(password, ALG),
        admin=admin,)
    db.session.add(user)

    # TODO: try/except fazer caso exista ja o user exista

    db.session.commit()
    return user


def save_user_foto(filename, filestorage):
    """
        Save users foto in ./upload/foo/fsdfsdf.ext

    """
    filename = os.path.join(
            app.config["UPLOAD_FOLDER"],
            secure_filename(filename)
    )
    filestorage.save(filename)
