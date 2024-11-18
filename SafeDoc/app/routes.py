from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from app import app, db
from app.models import User
from app.utils.face_recognition import analyze_image

# Função para verificar se o arquivo tem uma extensão permitida
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        photo = request.files['photo']
        document = request.files['document']

        if photo and allowed_file(photo.filename) and document and allowed_file(document.filename):
            # Salvar foto e documento
            photo_filename = secure_filename(photo.filename)
            document_filename = secure_filename(document.filename)

            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], 'photos', photo_filename)
            document_path = os.path.join(app.config['UPLOAD_FOLDER'], 'documents', document_filename)

            # Criar diretórios se não existirem
            os.makedirs(os.path.dirname(photo_path), exist_ok=True)
            os.makedirs(os.path.dirname(document_path), exist_ok=True)

            photo.save(photo_path)
            document.save(document_path)

            # Analisar imagem para verificar se contém uma pessoa
            analysis_result = analyze_image(photo_path)

            if not analysis_result:
                return "A imagem não contém uma pessoa válida. Tente novamente."

            # Salvar dados no banco de dados
            user = User(name=name, email=email, photo=photo_path, document=document_path)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('consult'))

    return render_template('register.html')

@app.route('/consult')
def consult():
    users = User.query.all()  # Consulta no banco de dados
    return render_template('consult.html', users=users)
