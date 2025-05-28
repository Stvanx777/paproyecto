import time
start = time.time()

print("[0.0s] Importando Flask")
from flask import Flask, redirect, url_for

print("[{:.2f}s] Importando extensiones".format(time.time() - start))
from .extensions import db, login_manager

def create_app():
    print("[{:.2f}s] Inicializando Flask".format(time.time() - start))
    app = Flask(__name__)

    print("[{:.2f}s] Cargando configuración".format(time.time() - start))
    app.config.from_object('config.Config')

    print("[{:.2f}s] Inicializando extensiones".format(time.time() - start))
    db.init_app(app)
    login_manager.init_app(app)

    print("[{:.2f}s] Importando modelos".format(time.time() - start))
    from .models import User, Question, Answer

    print("[{:.2f}s] Importando rutas".format(time.time() - start))
    from .routes.auth import auth_bp
    from .routes.questions import questions_bp
    from .routes.answers import answers_bp

    print("[{:.2f}s] Registrando blueprints".format(time.time() - start))
    app.register_blueprint(auth_bp)
    app.register_blueprint(questions_bp)
    app.register_blueprint(answers_bp)

    print("[{:.2f}s] Creando ruta raíz".format(time.time() - start))
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    print("[{:.2f}s] App creada exitosamente".format(time.time() - start))
    return app