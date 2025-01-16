from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.models import Usuario, Encuesta
from flask_login import login_user, logout_user, login_required

@app.route('/')
def index():
    encuestas = Encuesta.query.all()
    return render_template('index.html', encuestas=encuestas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = Usuario.query.filter_by(username=username).first()
        if usuario and usuario.password == password:
            login_user(usuario)
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    pass

@app.route('/encuesta/nueva', methods=['GET', 'POST'])
@login_required
def nueva_encuesta():
    return render_template('nueva_encuesta.html')

