from project_files.form import registraion_form, login_form
from project_files import app
from flask import render_template, url_for, flash, redirect

posts=[
    {
        'author':'shreekant nandiyawar',
        'title':'My first post',
        'content':'First post content',
        "date_posted":"March 23, 2023"
    },
    {
        'author':'shreekant nandiyawar',
        'title':'My second post',
        'content':'Second post content',
        "date_posted":"March 23, 2023"
    }
]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/register',methods=['POST','GET'])
def register_page():
    form=registraion_form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!!','success')
        return redirect(url_for('home_page'))
    return render_template('register.html',form=form)

@app.route('/login')
def login_page():
    form=login_form()
    return render_template('layout.html',form=form)