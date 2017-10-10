from .utils import get_user_history
from flask import Flask, request, render_template, Markup, flash, redirect, url_for
from flask_nav import Nav
from flask_wtf import Form
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_nav.elements import Navbar, View
import pandas as pd
from datetime import datetime

from wtforms import SelectField, TextField, SubmitField
from markdown import markdown
import json
import os

def create_app(configfile='config.py'):
    app = Flask(__name__)

    AppConfig(app, configfile)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        # form = AnalyzeForm(request.form)
        result = []
        with open("survey_website/data/questions.json") as data_file:
            questions = json.load(data_file)
        if request.method == 'POST':
            if app.config['DOWN']:
                messages = [
                    "Hi, we are making changes to this tool.",
                    "Will be back soon!"
                ]

                flash(' '.join(messages), 'error')
            else:
                print(request.form.to_dict())
                result = request.form.to_dict()
                print(result)
                return redirect(url_for('success'))
        return render_template('index.html', questions = questions)

    @app.route('/success', methods=['GET'])
    def success():
        return render_template('success.html')
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
