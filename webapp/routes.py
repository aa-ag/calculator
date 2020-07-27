from flask import render_template, request
from webapp import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        i = request.form['i']
        ii = request.form['ii']
        operation = request.form['operation']

        if operation == 'add':
            result = float(i) + float(ii)
            return render_template('home.html', result = result)
        
        elif operation == 'substract':
            result = float(i) - float(ii)
            return render_template('home.html', result = result)
        
        elif operation == 'multiply':
            result = float(i) * float(ii)
            return render_template('home.html', result = result)
        
        elif operation == 'divide':
            result = float(i) / float(ii)
            return render_template('home.html', result = result)
        
        else:
            return render_template('home.html')