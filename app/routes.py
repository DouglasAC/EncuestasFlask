from flask import render_template, flash, redirect, request, url_for
from app import app, db
from app.models import Usuario, Encuesta
from flask_login import login_user, logout_user, login_required
from app.forms import RegistrationForm

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
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = Usuario.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('⚠️ El nombre de usuario ya está en uso', 'danger')
            return render_template('register.html', form=form)
        
        existing_email = Usuario.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash('⚠️ El correo electrónico ya está en uso', 'danger')
            return render_template('register.html', form=form)
        
        user = Usuario(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('✅ ¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/encuesta/nueva', methods=['GET', 'POST'])
@login_required
def nueva_encuesta():
    return render_template('nueva_encuesta.html')

