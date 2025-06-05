from dataclasses import asdict
from http import HTTPStatus

import pytest
from sqlalchemy import select

from app.models import User


@pytest.mark.asyncio
async def test_create_user(client, session):
    response = client.post(
        '/conta/',
        json={
            'username': ' Thiago Eidi HAMada',
            'cpf': '343213131',
            'email': 'teste@teste.com',
            'senha': '123',
        },
    )

    user_db = await session.scalar(select(User).where(User.cpf == '343213131'))

    assert asdict(user_db) == {
        'username': 'thiago eidi hamada',
        'cpf': '343213131',
        'email': 'teste@teste.com',
        'senha': '123',
        'id': 1,
    }
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'thiago eidi hamada',
        'email': 'teste@teste.com',
        'id': 1,
    }


@pytest.mark.asyncio
async def test_create_user_with_same_email(user, client, session):
    response = client.post(
        '/conta/',
        json={
            'username': 'teste',
            'cpf': '123123',
            'email': user.email,  # Agora funciona sem erro!
            'senha': '123',
        },
    )

    user_db = await session.scalar(
        select(User).where(User.email == user.email)
    )
    assert user_db is None  # Assumindo que a API rejeitou por email duplicado
    assert response.status_code == HTTPStatus.CONFLICT


def test_create_user_with_same_cpf(user, client):
    response = client.post(
        '/conta/',
        json={
            'username': 'teste',
            'cpf': user.cpf,
            'email': 'teste@ofpaofpa.cpm',
            'senha': '123',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT
