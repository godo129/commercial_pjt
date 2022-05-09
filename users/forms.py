from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import get_user_model


User = get_user_model()


# 사용해보고 필요한 것만 놔두고 빼거나 커스텀할 것 
class  CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class CustomLoginForm(AuthenticationForm):
    fields = 'all'

