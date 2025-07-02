import pytest
from app import app as flask_app, db
from faker import Faker
from model.usuario_model import Usuario

fake = Faker()

@pytest.fixture(scope="session")
def app_context():
    """
    Fornece o contexto da aplicação com o banco SQLite em memória.
    Cria e limpa o schema uma única vez.
    """
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })

    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def db_session():
    """
    Limpa a sessão após cada teste.
    """
    yield db.session
    db.session.rollback()


@pytest.fixture
def usuario_fake(db_session):
    """
    Insere um usuário fake no banco e retorna o objeto.
    """
    usuario = Usuario(nome=fake.name(), email=fake.email())
    db_session.add(usuario)
    db_session.commit()
    return usuario


@pytest.fixture
def client(app_context):
    """
    Fornece o test client com contexto e banco configurado.
    """
    return app_context.test_client()
