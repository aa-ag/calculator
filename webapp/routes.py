from flask import render_template, request, redirect, url_for, flash, jsonify
from webapp import app, db, socketio, send
from webapp.models import Op

# from flask_socketio import SocketIO, send, emit

@app.route('/')
def home():
    all_ops = Op.query.all()[-10:][::-1]
    return render_template('home.html', all_ops = all_ops)

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':

        i = request.form['i']
        ii = request.form['ii']
        operation = request.form['operation']

        result = None

        try:
            if operation == '+' and type(float(i)) == float and type(float(ii)) == float:
                result = f'{i} + {ii} = {round(float(i) + float(ii), 2)}'
            
            elif operation == '-' and type(float(i)) == float and type(float(ii)) == float:
                result = f'{i} - {ii} = {round(float(i) - float(ii), 2)}'
            
            elif operation == 'x' and type(float(i)) == float and type(float(ii)) == float:
                result = f'{i} x {ii} = {round(float(i) * float(ii), 2)}'
            
            elif operation == '÷' and type(float(i)) == float and type(float(ii)) == float:
                result = f'{i} ÷ {ii} = {round(float(i) / float(ii), 2)}'

            if result != None:
                op = Op(result)
                db.session.add(op)
                db.session.commit()

                return jsonify(result=result, isValid=True)
        except:
            return jsonify(result="This is awkward... Right now I can only handle numbers. Try again :)", isValid=False)

# Calculator-looking GUI -- future iteration

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/math')
def math():
    return redirect(url_for('calculator'))
