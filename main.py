from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/signup", methods=['POST'])
def error():
    name = request.form['username']
    password = request.form['user_password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(name) < 3 or len(name) > 20:
        username_error = 'Not a valid username'
    
    if len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password"

    if verify_password != password:
        verify_error = "Passwords don't match"
    
    if len(email) != 0:
        if len(email) == 1 or len(email) == 2 or len(email) ==3 or len(email) > 20  or '@' not in email or '.' not in email or " " in email:
            email_error = "Not a valid email"

    if not password_error and not username_error and not verify_error and not email_error:
        return render_template("greeting.html",username=name)
    else:
        return render_template("user_signup.html",
            username_error=username_error,
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error)



@app.route("/")
def index():  
    return render_template('user_signup.html')

app.run()

