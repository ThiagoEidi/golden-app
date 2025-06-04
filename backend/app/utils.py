import re

from sqlalchemy.exc import IntegrityError


def sanitizar_name(username: str) -> str:
    username = username.lower()
    username = re.sub(r'[^a-z\s]', '', username)
    username = re.sub(r'\s+', ' ', username).strip()

    return username


def handle_integrity_error(error: IntegrityError) -> str:
    dicio = {
        'users_email_key': 'email já cadastrado',
        'users_cpf_key': 'cpf já cadastrado',
    }

    key = error.args[0].split('"')[1]

    return dicio[key]
