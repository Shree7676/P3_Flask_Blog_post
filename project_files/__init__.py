from flask import Flask,render_template

app=Flask(__name__)
app.config['SECRET_KEY']='2a686626a288921c7fb2eca327e9e774'

from project_files import routes