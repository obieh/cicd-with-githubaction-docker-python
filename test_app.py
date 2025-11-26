from app import app, db, Todo
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        t = Todo(content='sample task', complete=False)
        db.session.add(t)
        db.session.commit()
        client = app.test_client()
        yield client
        db.session.remove()
        db.drop_all()

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_edit_page(client):
    # ensure the edit page for the created todo returns 200
    with app.app_context():
        todo = Todo.query.first()
        assert todo is not None
        resp = client.get(f'/edit/{todo.id}')
        assert resp.status_code == 200