from dataclasses import asdict

import pytest
from sqlalchemy import select

from app.models import User


@pytest.mark.asyncio
async def test_create_user_database(session):
    new_user = User(
        username='thiago',
        cpf='1234567900',
        email='algum@email.com',
        senha='123',
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    user_db = await session.scalar(
        select(User).where(User.cpf == '1234567900')
    )

    assert asdict(user_db) == {
        'username': 'thiago',
        'cpf': '1234567900',
        'email': 'algum@email.com',
        'senha': '123',
        'id': 1,
    }
