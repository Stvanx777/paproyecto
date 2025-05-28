#print("Antes de importar create_app")

from app import create_app

#print("Después de importar create_app")

app = create_app()

#print("Después de llamar create_app")

if __name__ == '__main__':
    app.run(debug=True)
