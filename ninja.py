from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'ThisIsSecret'

import random
import datetime

def gold(start, end):
    gold = random.randrange(start,end)
    return gold


@app.route ('/')
def index():
    if session.get('total')==None:
        session['total']=0
    if session.get('activity')==None:
        session['activity']=[]
    return render_template('index.html', total=session['total'], activities=session['activity'])

@app.route('/process_money', methods=['POST'])
def Money():
    hiddenInput = request.form['hidden']
    if hiddenInput== 'farm':
        Gold = gold(10,21)
        session['total']+=Gold
    elif hiddenInput == 'cave':
        Gold = gold(5,11)
        session['total']+=Gold
    elif hiddenInput == 'house':
        Gold = gold(2,6)
        session['total']+=Gold
    elif hiddenInput == 'casino':
            Gold = gold(-51,51)
            session['total']+=Gold


    activity = ''
    time = datetime.datetime.now().strftime('%m/%d/%Y %I:%M %p')
    if Gold>=0:
        activity += 'You won ' + str(Gold) + ' golds from the ' + str(request.form['hidden'])
    else:
        activity += 'You came to the casino and made a deposit of' + str(Gold) +'golds!'


    activity += '! (' + str(time) + ')'
    session['activity'].insert(0, activity)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def zero():
    session['total']=0
    session['activity']=[]
    return redirect('/')

app.run(debug=True)
