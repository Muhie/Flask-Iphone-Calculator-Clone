from tempfile import template
import flask
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def home_page():
    return render_template('home_page.html')

if __name__ == "__main__":
     application.run(debug=True, host='0.0.0.0', port=8080)