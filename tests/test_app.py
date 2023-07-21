import pytest
from app import app

app.config['testing'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert rv.status_code == 200

    rv = web.get('/hello', follow_redirects=True)
    assert rv.status_code == 404
    assert b"Fill Out This Form", rv.data

