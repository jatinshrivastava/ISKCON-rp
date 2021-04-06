from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from users.models import CustomUser

# UserModel = get_user_model()


class MobilePhoneOrEmailModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        # the username could be either one of the two
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'phone_number': username}
        try:
            user = CustomUser.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return CustomUser.objects.get(pk=username)
        except CustomUser.DoesNotExist:
            return None
