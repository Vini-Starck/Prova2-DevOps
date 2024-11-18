from app import db

# Criação do banco de dados e tabelas
def init_db():
    db.create_all()

# Inicialização do banco de dados no início da aplicação
init_db()
