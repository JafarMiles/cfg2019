from flask import Flask, render_template, redirect, request
from datetime import datetime

app = Flask("ToyApp")

statusList = [{'status': 'hello world', 'username': 'Jaf', 'time': '18:40'}, {'status': 'yes please', 'username': 'Jaf', 'time': '18:42'}]


@app.route("/")
def hello():
    return render_template('index.html', feed=statusList)


@app.route("/addnote", methods=['POST'])
def addnote():
    form_data = request.form
    status = form_data['status']
    username = form_data['username']
    time = datetime.now().strftime('%H:%M');
    statusList.append({'status': status, 'username': username, 'time':time})
    return redirect('/')


app.run(debug=True)


# use ngrok!