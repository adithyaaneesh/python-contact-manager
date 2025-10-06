from django import forms
from django.contrib.auth.models import User
from .models import Contact


class UserRegistrationForm(forms.ModelForm):
    role = forms.ChoiceField(choices=Contact.ROLE_CHOICES)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username' , 'email']


    def clean(self):
        data = super().clean()
        if data.get('password') != data.get('password2'):
            raise forms.ValidationError("Password do not match")
        return data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Contact.objects.create(
                name=user,
                role=self.cleaned_data['role']
            )
        return user