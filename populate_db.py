import random
from faker import Faker
from app import app, db
from app.models import Usuario, Encuesta, Pregunta, Respuesta

fake = Faker()

def poblar_base_de_datos():
    with app.app_context():
        # Limpiar base de datos (opcional)
        # db.drop_all()
        # db.create_all()

        # Crear Usuarios
        usuarios = [Usuario(username=fake.name(), email=fake.email()) for _ in range(15)]
        for usuario in usuarios:
            usuario.set_password('password')
        db.session.add_all(usuarios)
        db.session.commit()

        # Crear Encuestas
        encuestas = [Encuesta(titulo=fake.sentence(), descripcion=fake.text(), usuario_id=random.choice(usuarios).id) for _ in range(6)]
        db.session.add_all(encuestas)
        db.session.commit()

        # Crear Preguntas para cada encuesta
        preguntas = []
        for encuesta in encuestas:
            for _ in range(random.randint(4, 6)):  # 4-6 preguntas por encuesta
                preguntas.append(Pregunta(texto=fake.sentence(), encuesta_id=encuesta.id))

        db.session.add_all(preguntas)
        db.session.commit()

        # Crear Respuestas
        respuestas = []
        for usuario in usuarios:
            encuestas_respondidas = random.sample(encuestas, random.randint(4, 6))  # Cada usuario responde 4-6 encuestas
            for encuesta in encuestas_respondidas:
                preguntas_encuesta = [p for p in preguntas if p.encuesta_id == encuesta.id]
                for pregunta in preguntas_encuesta:
                    respuestas.append(Respuesta(
                        texto=fake.sentence(),
                        pregunta_id=pregunta.id,
                        usuario_id=usuario.id
                    ))

        db.session.add_all(respuestas)
        db.session.commit()

        print("🚀 Datos de prueba generados con éxito!")

if __name__ == "__main__":
    poblar_base_de_datos()
