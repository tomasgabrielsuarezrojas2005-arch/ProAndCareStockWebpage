from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Flask busca automáticamente dentro de la carpeta 'templates'
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    correo_ingresado = request.form.get('correo')
    contrasena_ingresada = request.form.get('contrasena')   
    
    with open('usuarios.txt', 'r') as user_pass:
        for contra_user in user_pass:
            resultado= contra_user.strip().split(",")
            if len(resultado) == 2:
                correo_txt = resultado[0]
                contrasena_txt = resultado[1]
                if correo_ingresado==correo_txt and contrasena_ingresada==contrasena_txt:
                    return ("sesión iniciada correctamente")
    return ("Usuario o contraseña no válidos")