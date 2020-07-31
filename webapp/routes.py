from flask import render_template, request, redirect, url_for, flash
from webapp import app, db
from webapp.models import Op

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

        try:
            if operation == '+' and type(float(i)) == float and type(float(ii)) == float:
                result = f'{i} + {ii} = {round(float(i) + float(ii), 2)}'

                op = Op(result)
                db.session.add(op)
                db.session.commit()

                return redirect(url_for('home'))
            
            elif operation == '-' and type(float(i)) == float and type(float(ii)) == float:
                result = f'{i} - {ii} = {round(float(i) - float(ii), 2)}'

                op = Op(result)
                db.session.add(op)
                db.session.commit()

                return redirect(url_for('home'))
            
            elif operation == 'x' and type(float(i)) == float and type(float(ii)) == float:
                result = f'{i} x {ii} = {round(float(i) * float(ii), 2)}'

                op = Op(result)
                db.session.add(op)
                db.session.commit()

                return redirect(url_for('home'))
            
            elif operation == '÷' and type(float(i)) == float and type(float(ii)) == float:
                result = f'{i} ÷ {ii} = {round(float(i) / float(ii), 2)}'

                op = Op(result)
                db.session.add(op)
                db.session.commit()

                return redirect(url_for('home'))
        except:
            flash("This is awkward... Right now I can only handle numbers. Try again :)")
            return redirect(url_for('home'))

# Calculator-looking GUI -- future itereation

@app.route('/calculator')
def calc():
    return render_template('calculator.html')

@app.route('/math')
def math():
    return redirect(url_for('calculator'))
