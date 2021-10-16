from flask_wtf import Form, RecaptchaField

class RegisterForm(Form):
    recaptcha = RecaptchaField()