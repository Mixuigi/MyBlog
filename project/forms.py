from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", help_text='введите своё имя')
    age = forms.IntegerField(label="Возраст", initial= 0, help_text='введите возраст', required= False)
    country = forms.ChoiceField(choices=(("English", 1), (2, "German"), (3, "French")), required= False)