from flask import Flask, request, render_template, redirect, flash
from app.models import User
from app.db import db
from app.utils.face_recognition import verify_face
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://azureadmin:Admsenac123@a@sqlserver-safedoc.database.windows.net/SafeDocDb?driver=ODBC+Driver+17+for+SQL+Server'
app.config['UPLOAD_FOLDER'] = 'uploads'
db.init_app(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        photo = request.files['photo']
        document = request.files['document']

        # Salvar arquivos temporariamente
        photo_path = os.path.join(app.config['UPLOAD_FOLDER'], 'photos', photo.filename)
        document_path = os.path.join(app.config['UPLOAD_FOLDER'], 'documents', document.filename)
        photo.save(photo_path)
        document.save(document_path)

        # Verificar rosto na foto usando o Serviço Cognitivo
        if not verify_face(photo_path):
            flash('Imagem inválida: não foi detectado um rosto humano.')
            return redirect('/register')

        # Registrar usuário no banco
        new_user = User(name=name, email=email, photo_path=photo_path, document_path=document_path)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuário registrado com sucesso!')
        return redirect('/consult')

    return render_template('register.html')

@app.route('/consult', methods=['GET', 'POST'])
def consult():
    if request.method == 'POST':
        name = request.form['name']
        users = User.query.filter_by(name=name).all()
        return render_template('consult.html', users=users)
    return render_template('consult.html', users=None)

