import os
import tempfile

import pytest

from flasktodo import run


@pytest.fixture
def client():
    db, flasktodo.run.config['DATABASE'] = tempfile.mkstemp()
    flasktodo.app.config['TESTING'] = True

    with flasktodo.app.test_client() as client:
        with flasktodo.app.app_context():
            flasktodo.init_db()
        yield client

    os.close(db)
    os.unlink(flasktodo.app.config['DATABASE'])


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)
