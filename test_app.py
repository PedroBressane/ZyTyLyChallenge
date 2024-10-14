import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_register_user_large_username(client):
    large_username = 'a' * 51
    response = client.post('/user/register', json={
        'username': large_username,
        'email': 'test@example.com',
        'password': 'Password123!'
    })
    assert response.status_code == 400
    assert b"Bad Request" in response.data

def test_register_user_valid_data(client):
    response = client.post('/user/register', json={
        'username': 'A__&&&11467JJJtestp-wd111!!!',
        'email': 'test@zylyty.com',
        'password': 'Password123!'
    })
    assert response.status_code == 201
    assert b"Registration was successful." in response.data
#