from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, PasswordField
from wtforms import validators, ValidationError

class helpForm(Form):
    
    """
    Help form for Partners: To be accessed through the partners FAQ pages.
    """
    name = TextField("Name", [validators.Required("Enter Your Name")])
    tel = TextField("Phone", [validators.Required("Phone Number?")])
    email = TextField("Email", [validators.Required("Email"), validators.email("Enter Correct email")])
    location = TextField("Your Locale", [validators.Required("Location")])
    issue = SelectField('Issue', choices=[('service', 'Service'), ('accident', 'Accident'), ('registration', 'Registration'), ('availability', 'Availabilty'), ('account', 'Account')])
    report = TextAreaField('Report')

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)

class LoginForm(Form):
    
    """
    Login form for Partners: To be used before editing stuff first.
    """

    email = TextField("Email", [validators.Required("Email"), validators.email("Enter Correct email")])
    password = PasswordField('Password', [validators.DataRequired()])
