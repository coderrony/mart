from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {'class':  'w-full   px-4 py-2 rounded-lg shadow-sm focus:outline-none focus:shadow-outline-gray'})
