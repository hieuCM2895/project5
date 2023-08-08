from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='This is capstore project', name='hieucm2')

app.run(host='0.0.0.0', port=80)