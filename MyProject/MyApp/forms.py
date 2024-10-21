from django import forms

class PasswordForm(forms.Form):
    length = forms.IntegerField(label='Password Length', min_value=4, max_value=50)
    use_uppercase = forms.BooleanField(label='Include Uppercase Letters', required=False)
    use_numbers = forms.BooleanField(label='Include Numbers', required=False)
    use_symbols = forms.BooleanField(label='Include Symbols', required=False)
