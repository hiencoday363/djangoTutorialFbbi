from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ..models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [i.name for i in User._meta.fields]
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }
        exclude = ('username',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = [i.name for i in User._meta.fields]
        widgets = {
            'date_of_birth': DateInput(attrs={'type': 'date'}),
        }

    exclude = ('username',)
