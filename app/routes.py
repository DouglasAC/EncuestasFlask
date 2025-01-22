from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Usuario, Encuesta, Pregunta, Respuesta
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import RegistrationForm, LoginForm, EncuestaForm, RespuestaForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('⚠️ Nombre de usuario o contraseña inválidos', 'danger')
            return render_template('login.html', form=form)
        
        login_user(user, remember=form.remember.data)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

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

@app.route('/dashboard')
@login_required
def dashboard():
    pass

@app.route('/crear_encuesta', methods=['GET', 'POST'])
@login_required
def crear_encuesta():
    form = EncuestaForm()
    if form.validate_on_submit():
        encuesta = Encuesta(
            titulo=form.titulo.data, 
            descripcion=form.descripcion.data, 
            usuario_id=current_user.id)
        db.session.add(encuesta)
        db.session.commit()

        for pregunta_form in form.preguntas.data:
            pregunta = Pregunta(texto=pregunta_form['texto'], encuesta_id=encuesta.id)
            db.session.add(pregunta)

        db.session.commit()

        flash('✅ Encuesta creada exitosamente', 'success')
        return redirect(url_for('index'))
    else:
        print(form.errors)
    return render_template('crear_encuesta.html', form=form)

@app.route('/encuestas')
def listar_encuestas():
    page = request.args.get('page', 1, type=int)
    serch_query = request.args.get('q', '', type=str)

    if serch_query:
        encuestas = Encuesta.query.filter(Encuesta.titulo.ilike(f'%{serch_query}%'))
    else:
        encuestas = Encuesta.query

    encuestas = encuestas.paginate(page=page, per_page=5, error_out=False)
    return render_template('listar_encuestas.html', encuestas=encuestas, serch_query=serch_query)


@app.route('/encuesta/<int:encuesta_id>')
def ver_encuesta(encuesta_id):
    encuesta = Encuesta.query.get_or_404(encuesta_id)  # Obtener encuesta o mostrar error 404
    preguntas = Pregunta.query.filter_by(encuesta_id=encuesta_id).all()
    
    return render_template('ver_encuesta.html', encuesta=encuesta, preguntas=preguntas)

@app.route('/encuesta/<int:encuesta_id>/responder', methods=['GET', 'POST'])
@login_required
def responder_encuesta(encuesta_id):
    encuesta = Encuesta.query.get_or_404(encuesta_id)
    preguntas = Pregunta.query.filter_by(encuesta_id=encuesta_id).all()
    respuestas_existentes = Respuesta.query.filter_by(usuario_id=current_user.id).filter(
        Respuesta.pregunta_id.in_([p.id for p in preguntas])
    ).all()
    
    if respuestas_existentes:
        flash('⚠️ Ya has respondido esta encuesta.', 'warning')
        return render_template('ver_respuesta.html', encuesta=encuesta, respuestas=respuestas_existentes)
    
    
    form = RespuestaForm(preguntas)
    
    if form.validate_on_submit():
        for pregunta in preguntas:
            field_name = f'pregunta_{pregunta.id}'
            respuesta_texto = getattr(form, field_name).data
            respuesta = Respuesta(texto=respuesta_texto, pregunta_id=pregunta.id, usuario_id=current_user.id, encuesta_id=encuesta_id)
            db.session.add(respuesta)
            
        db.session.commit()
        flash('✅ Respuestas enviadas exitosamente', 'success')
        return redirect(url_for('ver_respuesta', encuesta_id=encuesta.id))
    else:
        print(form.errors)
    return render_template('responder_encuesta.html', encuesta=encuesta, preguntas=preguntas, form=form)

@app.route('/encuesta/<int:encuesta_id>/ver_respuesta')
@login_required
def ver_respuesta(encuesta_id):
    encuesta = Encuesta.query.get_or_404(encuesta_id)
    respuestas = Respuesta.query.filter_by(usuario_id=current_user.id, encuesta_id=encuesta_id).all()
    
    return render_template('ver_respuesta.html', encuesta=encuesta, respuestas=respuestas)