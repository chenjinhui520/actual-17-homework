# encoding: utf-8

from flask import Flask

app = Flask(__name__)
app.secret_key = '13123dfasdf'

import views
