from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://azureadmin:Admsenac123@a@sqlserver-safedoc.database.windows.net/SafeDocDb?driver=ODBC+Driver+17+for+SQL+Server'  # Usando SQLite para simplificação
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Diretório para uploads

# Inicializa o banco de dados
db = SQLAlchemy(app)

# Importando as rotas
from app import routes
