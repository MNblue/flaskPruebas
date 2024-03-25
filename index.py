from src import app
from flask import Flask, render_template, request, redirect, url_for
import suma




@app.route('/')

def index():
    # pasamos datos a la pagina html
    datos = ['dato1', 'dato2', 'dato3']
    return render_template('index.html', datos=datos)

#mostramos varios input en index.html y su valores recogemos aqui y los pasamos a suma.py y nos da el resultado y este resultado se pasa  pagina2.html
#  Esto es un decorador en Python que define una ruta en tu aplicación Flask. En este caso, cuando alguien realiza una solicitud HTTP 
# a la ruta /realizar_operacion con el método POST (generalmente utilizado para enviar datos), Flask ejecutará la función realizar_operacion().
# @app.route('/realizar_operacion', methods=['POST'])

#  Esta es la definición de la función realizar_operacion(). Esta función se ejecutará cuando se haga una solicitud a la ruta /realizar_operacion con el método POST.
def realizar_operacion():
    #  Aquí estamos obteniendo el valor del campo valor1 del formulario enviado con la solicitud POST. request.form es un
    #  diccionario que contiene los datos enviados con el formulario. Luego convertimos este valor a un entero 
    valor1 = int(request.form['valor1'])
    valor2 = int(request.form['valor2'])
    resultado = suma.sumar(valor1, valor2)  # Llama a la función sumar de suma.py
    #  Finalmente, redirigimos la solicitud a otra ruta utilizando redirect() y url_for().
    # Aquí estamos redirigiendo a la función mostrar_resultado() y pasando el resultado de la suma como un parámetro llamado resultado.
    return redirect(url_for('mostrar_resultado', resultado=resultado))


# Este es otro decorador en Python que define una ruta en tu aplicación Flask. En este caso, la ruta es /mostrar_resultado/<resultado>,
# donde <resultado> es una variable que puede ser parte de la URL y que será capturada por Flask y pasada como argumento a la función mostrar_resultado
@app.route('/mostrar_resultado/<resultado>')
# Esta es la definición de la función mostrar_resultado(). Esta función se ejecutará cuando alguien haga una solicitud a la ruta /mostrar_resultado/<resultado>.
def mostrar_resultado(resultado):
# Aquí estamos utilizando la función render_template() para renderizar una plantilla HTML llamada pagina2.html. 
# Además, estamos pasando una variable llamada resultado a la plantilla HTML. 
# Esta variable contendrá el valor capturado en la URL (en este caso, el resultado de la operación matemática realizada anteriormente).
# Esto permitirá que la plantilla HTML acceda a este valor y lo muestre en la página.    
    return render_template('pagina2.html', resultado=resultado)


if __name__ == '__main__':

    app.run()