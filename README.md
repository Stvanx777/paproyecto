# Code Cram

**Code Cram** es una aplicación web sencilla donde los usuarios pueden publicar preguntas, ver las preguntas de otros usuarios y responderlas. Cuando el autor de una pregunta obtiene una respuesta satisfactoria, puede eliminar su pregunta o hacerlo en cualquier momento.

Este proyecto fue desarrollado como una práctica escolar, enfocado en poner en práctica conceptos de desarrollo web con Flask y operaciones CRUD básicas.

---

## 🚀 Funcionalidades

- Registro e inicio de sesión de usuarios.
- Creación de preguntas.
- Visualización de preguntas recientes.
- Responder a preguntas de otros usuarios.
- Eliminación de preguntas por parte del autor.

---

## 🛠 Tecnologías utilizadas

- Python 3
- Flask 3.1.1
- Flask-Login
- Flask-SQLAlchemy
- SQLite3
- Jinja2
- HTML/CSS

---

## 📁 Estructura del proyecto

```
cc/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models.py
│   ├── routes/
│   │   ├── answers.py
│   │   ├── auth.py
│   │   └── questions.py
│   ├── static/
│   │   └── styles.css
│   └── templates/
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       └── questions/
│           ├── ask.html
│           ├── detail.html
│           └── list.html
├── config.py
├── create_db.py
├── run.py
├── requirements.txt
└── studentoverflow.db
```

---

## 💻 Instalación y ejecución local

1. Clona el repositorio o copia los archivos.
2. Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala los requerimientos:

```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:

```bash
python run.py
```

5. Abre tu navegador y entra a `http://localhost:5000`.

---

## 📜 Licencia

Este proyecto está bajo la licencia [The Unlicense](https://unlicense.org/), lo que significa que puedes usarlo, modificarlo o distribuirlo sin ninguna restricción.

---

## ✍️ Autor

Esteban Antonio Serrano Morales  
Proyecto creado con fines educativos.
