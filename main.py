from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')


# ejercicio 1
@app.route('/ejercicio_1')
def ejercicio_1():
    return render_template('Ejercicio_1.html')

# ejercicio 2
@app.route('/ejercicio_2')
def ejercicio_2():
    return render_template('Ejercicio_2.html')


if __name__ == '__main__':
    app.run(debug=True)