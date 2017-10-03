from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():    
    return render_template('user_signup.html')

@app.route("/welcome", methods=['POST'])
def welcome():
    name = request.form['username']

    username_error = ''
    if len(name) < 3 or len(name) > 20:
        username_error = 'Not a valid username'
        return render_template('user_signup.html',username_error=username_error)

    password = request.form['password']
    password_error = ''
    if len(password) < 3 or len(password) > 20:
        password_error = "That's not valid password"
        return render_template('user_signup.html',password_error=password_error)

    return render_template('greeting.html',username=name)


app.run()

