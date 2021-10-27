import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Email, Length, EqualTo, ValidationError


def NameCharacter_check(form, field):
    excluded_chars = "*?!'^+%&/()=}][{$#@<>"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(
                f"Character {char} is not allowed.")


class RegisterForm(FlaskForm):
    email = StringField(validators=[Required(), Email()])
    firstname = StringField(validators=[Required(), NameCharacter_check])
    lastname = StringField(validators=[Required(), NameCharacter_check])
    phone = StringField(validators=[Required()])
    password = PasswordField(validators=[Required(), Length(min=6, max=12,
                                                            message='Password must be between 6 and 12 characters in length.')])
    confirm_password = PasswordField(
        validators=[Required(), EqualTo('password', message='Both password fields must be equal!')])
    pin_key = StringField(validators=[Required(), Length(min=32, max=32,
                                                         message='PIN Key must be 32 characters in length.')])

    submit = SubmitField()

    def register(self):
        form = RegisterForm()
        if form.validate_on_submit():
            return login()

    def validate_password(self, password):
        p = re.compile(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[#$%&*+,./:;!<>()=?@\[\]_`|{}~])')
        if not p.match(self.password.data):
            raise ValidationError("Password must contain at least 1 digit, 1 lowercase, 1 uppercase letter and 1 "
                                  "special character from #$%&*+,./:;<>()=!?@[]_`|{}~.")

    def validate_phone(self, phone):
        ph = re.compile(r'\d{4}-\d{3}-\d{4}$')
        if not ph.match(self.phone.data):
            raise ValidationError("Phone must be of the form XXXX-XXX-XXXX (including the dashes)")

class LoginForm(FlaskForm):
    email = StringField(validators=[Required(), Email()])
    password = PasswordField(validators=[Required()])
    submit = SubmitField()

