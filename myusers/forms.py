from django.forms import ModelForm
from .models import users

class UsersForm(ModelForm):
    class Meta:
        model = users