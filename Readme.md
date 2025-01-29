# Plataforma de Encuestas Online

## Descripción
Esta es una plataforma web desarrollada con Flask que permite a los usuarios crear encuestas personalizadas, responder preguntas y visualizar los resultados de las encuestas en un formato amigable.

## Tecnologías Utilizadas
- **Backend**: Python, Flask, Flask-Login, Flask-Migrate, Flask-SQLAlchemy
- **Base de Datos**: PostgreSQL
- **Frontend**: Jinja2, Bootstrap
- **Autenticación**: Flask-Login con sistema de usuarios

## Características
- Registro e inicio de sesión de usuarios
- Creación, edición y eliminación de encuestas
- Respuesta de encuestas por diferentes usuarios
- Visualización de resultados de encuestas con paginación
- Exportación de respuestas a CSV

## Instalación y Configuración
### Requisitos
- Python 3.8 o superior
- PostgreSQL
- Virtualenv (opcional pero recomendado)

### Pasos para instalar
1. Clonar el repositorio:
   ```sh
   git clone https://github.com/tu-usuario/EncuestasFlask.git
   ```
2. Crear y activar un entorno virtual:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # En macOS/Linux
   .venv\Scripts\activate     # En Windows
   ```
3. Instalar dependencias:
   ```sh
   pip install -r requirements.txt
   ```
4. Configurar la base de datos en `.env`:
   ```sh
   DATABASE_URL=postgresql://usuario:contraseña@localhost/nombre_bd
   SECRET_KEY = generar una clave secreta
   ```
5. Ejecutar migraciones:
   ```sh
   flask db upgrade
   ```
6. Iniciar la aplicación:
   ```sh
   flask run
   ```

## Uso
- Iniciar sesión o registrarse.
- Crear una nueva encuesta desde el panel de usuario.
- Agregar preguntas a la encuesta.
- Visualizar los resultados desde el panel de usuario.
- Exportar respuestas a CSV si es necesario.

## Capturas de Pantalla

- **Inicio**: Es la página de inicio.
    ![Inicio](imgs/inicio.png) 
- **Registro**: Es la página para registrarse.
    ![Registro](imgs/registro.png) 
- **Inicio de sección**: Es la página de inicio de sección.
    ![Inicio de sección](imgs/login.png)
- **Dashboard**: Se muestra el dashboard del usuario.
    ![Dashboard](imgs/dashboard.png)
- **Nueva encuesta**: Crear una nueva encuesta.
    ![Nueva encuesta](imgs/nueva_encuesta.png)
- **Responder encuesta**: Así se responde una encuesta.
    ![Responder encuest](imgs/ingresar_respuesta.png)
- **Ver encuestas**: Se muestran todas las encuestas.
    ![Ver encuestas](imgs/Encuestas.png)
- **Ver Respuestas**: Ver las respuestas ingresadas
    ![Ver Respuestas](imgs/respuestas.png) 


## Contribución
Si deseas contribuir, puedes hacer un fork del repositorio, crear una nueva rama y enviar un pull request.

---
¡Gracias por visitar este proyecto! 😊
