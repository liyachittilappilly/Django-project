from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    full_name = forms.CharField(label="Full Name")
    phone = forms.CharField(label="Phone Number")
    college = forms.CharField(label="College")
    degree = forms.CharField(label="Degree")
    branch = forms.CharField(label="Branch")

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match")
