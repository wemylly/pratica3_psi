from models import User, Book
from database import SessionLocal

with SessionLocal as session:
    usuario_inicial = User(nome="Maria", email="maria.com@gmail")
    livro_inicial = Book(titulo="Dom Casmurro", id_usuario=1)

    session.add(usuario_inicial)
    session.add(livro_inicial)

    session.commit()