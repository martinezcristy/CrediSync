from flask import Flask, render_template

app = Flask(_name_, static_folder='assets', static_url_path='/static')

@app.route('/')
def dashboard():
    return render_template('dashboard.html')