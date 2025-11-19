from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

# Ejercicio 1
VALOR_TARRO = 9000

@app.route('/ejercicio_1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None

    if request.method == 'POST':
        try:
            nombre = request.form['nombre'].strip()
            edad_texto = request.form['edad'].strip()
            tarros_texto = request.form['cantidad_tarros'].strip()

            if not nombre:
                raise ValueError("Debe ingresar un nombre")

            if not edad_texto:
                raise ValueError("Debe ingresar su edad")
            if not edad_texto.isdigit():
                raise ValueError("Debe ingresar un número válido para la edad")
            edad = int(edad_texto)
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")

            if not tarros_texto:
                raise ValueError("Debe ingresar la cantidad de tarros a comprar")
            if not tarros_texto.isdigit():
                raise ValueError("Debe ingresar un número válido para la cantidad de tarros")
            cantidad_tarros = int(tarros_texto)
            if cantidad_tarros < 1:
                raise ValueError("Debe comprar al menos un tarro")

            edad = int(edad_texto)
            cantidad_tarros = int(tarros_texto)

            total_sin_descuento = cantidad_tarros * VALOR_TARRO

            if edad >=18 and edad <= 30:
                porcentaje_descuento = 0.15
            elif edad > 30:
                porcentaje_descuento = 0.25
            else:
                porcentaje_descuento = 0

            monto_descuento = total_sin_descuento * porcentaje_descuento
            total_a_pagar = total_sin_descuento - monto_descuento

            resultado = {
                'nombre': nombre,
                'total_sin_descuento': total_sin_descuento,
                'monto_descuento': round(monto_descuento, 1),
                'total_a_pagar': round(total_a_pagar, 1),
                'porcentaje_descuento': int(porcentaje_descuento * 100)
            }

        except ValueError as e:
            resultado = {'error': str(e)}

    return render_template('Ejercicio_1.html', resultado=resultado)






#  Desarrollo ejercicio 2

USUARIOS_REGISTRADOS = {
    "juan": {"contrasena": "admin", "rol": "Administrador"},
    "pepe": {"contrasena": "user", "rol": "Usuario"}
}

@app.route('/ejercicio_2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        usuario_ingresado = request.form.get('usuario', '').lower()
        contrasena_ingresada = request.form.get('contrasena', '')

        usuario_info = USUARIOS_REGISTRADOS.get(usuario_ingresado)

        if usuario_info and usuario_info['contrasena'] == contrasena_ingresada:
            mensaje = f"Bienvenido {usuario_info['rol']} {usuario_ingresado}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio_2.html', mensaje=mensaje)

# Ejecución
if __name__ == '__main__':
    app.run(debug=True)