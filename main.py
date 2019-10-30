# If the user's form submission is not valid, you should reject it and re-render the form with some 
# feedback to inform the user of what they did wrong. The following things should trigger an error:

# The user leaves any of the following fields empty: username, password, verify password.
# The user's username or password is not valid -- for example, it contains a space character 
# or it consists of less than 3 characters or more than 20 characters (e.g., a username or password 
# of "me" would be invalid).

# The user's password and password-confirmation do not match.
# The user provides an email, but it's not a valid email. 
# Note: the email field may be left empty, but if there is content in it, then it must be validated. 
# The criteria for a valid email address in this assignment are that it has a single @, a single ., 
# contains no spaces, and is between 3 and 20 characters long.

# Each feedback message should be next to the field that it refers to.

# For the username and email fields, you should preserve what the user typed, 
# so they don't have to retype it. With the password fields, you should clear them, for security reasons.

# If all the input is valid, then you should show the user a welcome page that uses the username input 
# to display a welcome message of: "Welcome, [username]!"

# Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.
# While we've covered how to specify different input types than just text (e.g., password and email), 
# for this assignment do not use the email input type. Instead, just use text, which does not 
# do any client-side validation. This will enable us to check that the server side validation is working 
# by letting errors through the client side. You should, however, use type='password' for the password and 
# password verification inputs, to hide the characters typed (this input type does not include any additional validation).


from flask import Flask, render_template, redirect, request

import os

app = Flask(__name__)
app.config['DEBUG'] = True

#create route handler for the login page that creates placeholders inside the form:

@app.route('/')
def display_login_form():
    return render_template("signup.html", title="Signup")


#Create route hanlder for postiing to login form

@app.route('/login', methods = ["GET", 'POST'])
def validate_login():

#Create variables for pulling query parameters from form being posted using Flask Request Object -dictionary:
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

# create variables for error messages
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

#create validation for username:
    if username == '':
        username_error = "Username Error: Empty, please enter a name 4-20 characters long."
        username = ''

    if len(username) < 3 or len(username) > 20:
        username_error = "Username Error: Please enter a name 4-20 characters long."
        username = ''

    if ' ' in username:
        username_error = "Username Error: Space, please enter a name 4-20 characters long w/o spaces."
        username = ''


# Create validation for password:
    if password == '':
        pasword_error = "Password Error: Empty. Please enter a name 4-20 characters long."
        

    if len(password) < 3 or len(password) > 20:
        password_error = "Password Error: Please enter a name 4-20 characters long."
        

    if ' ' in password:
        password_error = "Password Error: Space. Please enter a name 4-20 characters long w/o spaces."
        

# Create validation for verify:
    if verify != password:
        verify_error = "Verify Error: Passwords do not match. Please renter both."
       

 #create validation for email:
    if email != '':
        if len(email) <3 or len(email) > 20:
            email_error = "Email Error: Please enter a email thats 4-20 characters long."
            email = ''

        if ' ' in email:
            email_error = "Password Error: Space. Please enter a name 4-20 characters long w/o spaces."
            eamil = ''
        
        if not email.count('@') == 1:
            email_error = "Email Error: Please enter a valid email."
            email = ''
            
        if not email.count('.') == 1:
            email_error = "Email Error: Please enter a valid email."
            email = ''

# Return template html pages for either 'welcome.html page' if form inputs are valid -or- login.html page showing all form input validation errors.
   
    if not username_error and not password_error and not verify_error and not email_error:
       #username = username  not needed as the variable 'username' value is held b/c either its global -or- this is still considered local area 
       return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('signup.html', username_error = username_error, password_error = password_error, 
        verify_error = verify_error, email_error = email_error, username = username, email = email, title=Signup)

# Create a route handler for Welcome page- passing in query parameter for username:

@app.route("/welcome", methods = ['GET'])
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html", title="Welcome", username=username)


app.run()