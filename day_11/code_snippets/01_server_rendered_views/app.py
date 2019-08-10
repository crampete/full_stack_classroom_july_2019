from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home/bad')
def bad():
    return '<html><head><title>Home Page - Bad</title></head><body><p>Welcome to the home page</p><p>This gets messy really fast.</p></body></html>'


@app.route('/home/good')
def good():
    return render_template('home.html')


app.run()
