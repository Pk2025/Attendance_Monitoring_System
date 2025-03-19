from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackEnd(ModelBackend):
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(f"EmailBackEnd: Authenticating {username}")
        try:
            user = UserModel.objects.get(email=username)
            print(f"EmailBackEnd: User found: {user.username}")
            if user.check_password(password):
                print("EmailBackEnd: Password check passed")
                return user
            else:
                print("EmailBackEnd: Password check failed")
        except UserModel.DoesNotExist:
            print("EmailBackEnd: User not found")
            return None
        return None