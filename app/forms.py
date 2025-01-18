from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FieldList, FormField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=128)])
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recordarme')
    submit = SubmitField('Iniciar sesión')

class PreguntaForm(FlaskForm):
    texto = StringField('Pregunta', validators=[DataRequired(), Length(min=3, max=500)])

class EncuestaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(), Length(min=3, max=200)])
    descripcion = StringField('Descripción', validators=[Length(max=500)])
    preguntas = FieldList(FormField(PreguntaForm), min_entries=1)
    submit = SubmitField('Crear encuesta')