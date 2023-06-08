from app.models import User, Pool
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Пароль",min_length=6, widget=forms.PasswordInput,required=True,validators = [RegexValidator(r"^[a-zA-Z0-9-]+$", message="Разрешена только латиница"),],)
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, required=True,validators = [RegexValidator(r"^[a-zA-Z0-9-]+$", message="Разрешена только латиница"),],)

    class Meta:
        model = User
        fields = ["name", "surname","username","email","password1","password2"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AddPoolForm(forms.ModelForm):
     name = forms.CharField(max_length=100)
     elo = forms.CharField(max_length=100)
     hours = forms.CharField(max_length=100)
     discord = forms.CharField(max_length=100)
     age = forms.CharField(max_length=100)
     nickname = forms.CharField(max_length=100)

