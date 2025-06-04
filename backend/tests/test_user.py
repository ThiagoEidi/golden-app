from http import HTTPStatus


def test_create_user(client):
    response = client.post(
        '/conta/',
        json={
            'username': ' Thiago Eidi HAMada',
            'cpf': '343213131',
            'email': 'teste@teste.com',
            'senha': '123',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'thiago eidi hamada',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_create_user_with_same_email(user, client):
    response = client.post(
        '/conta/',
        json={
            'username': 'teste',
            'cpf': '123123',
            'email': user.email,
            'senha': '123',
        },
    )
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
    __import__('ipdb').set_trace()
    assert response.status_code == HTTPStatus.CONFLICT
