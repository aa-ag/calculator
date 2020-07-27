from flask import render_template, request
from webapp import app, db
from webapp.models import Op

@app.route('/')
def home():
    all_ops = Op.query.limit(10).all()
    return render_template('home.html', all_ops = all_ops)

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':

        i = request.form['i']
        ii = request.form['ii']
        operation = request.form['operation']

        if operation == 'add':
            result = f'{i} + {ii} = {round(float(i) + float(ii), 2)}'

            op = Op(result)
            db.session.add(op)
            db.session.commit()

            return render_template('home.html', result = result)
        
        elif operation == 'substract':
            result = f'{i} - {ii} = {round(float(i) - float(ii), 2)}'

            op = Op(result)
            db.session.add(op)
            db.session.commit()

            return render_template('home.html', result = result)
        
        elif operation == 'multiply':
            result = f'{i} x {ii} = {round(float(i) * float(ii), 2)}'

            op = Op(result)
            db.session.add(op)
            db.session.commit()

            return render_template('home.html', result = result)
        
        elif operation == 'divide':
            result = f'{i} ÷ {ii} = {round(float(i) / float(ii), 2)}'

            op = Op(result)
            db.session.add(op)
            db.session.commit()

            return render_template('home.html', result = result)

        # else:
        #     return render_template('home.html')
            

# TO DO: catch erroneous inputs, 
# if time allows: Captcha, calculator GUI

# result = 'This is awkward... dunnot how to do that :s'
# return render_template('home.html', result = result)