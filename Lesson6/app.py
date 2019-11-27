from flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask("ToyApp")

statusList = [
    {
        'status': 'hello world',
        'username': 'Jaf',
        'mood': 'bored',
        'time': '18:40'
    },
    {
        'status': 'yes please',
        'username': 'Jaf',
        'mood': 'less bored',
        'time': '18:42'}
]


@app.route("/")
def hello():
    return render_template('index.html', feed=statusList)


@app.route("/addnote", methods=['POST'])
def addnote():
    form_data = request.form
    print(form_data)
    status = form_data['status']
    username = form_data['username']
    mood = form_data['mood']

    time = datetime.now().strftime('%H:%M');
    statusList.append({'status': status,
                       'username': username,
                       'time': time,
                       'mood': mood})
    return redirect('/')


app.run(debug=True)