from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from user_register.models import NewUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget = forms.PasswordInput)

    class Meta:
        model = NewUser
        fields = ['email', 'user_name', 'first_name', 'last_name', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget = forms.PasswordInput)

    class Meta:
        model = NewUser
        fields = ['email', 'user_name', 'first_name', 'last_name', 'is_staff', 'is_superuser']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = NewUser
        fields = ['email', 'user_name', 'first_name', 'last_name', 'password', 'is_staff', 'is_superuser']

    def clean_password(self):
        return self.initial['password'] 