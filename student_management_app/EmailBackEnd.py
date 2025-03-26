from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackEnd(ModelBackend):
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        print(f"EmailBackEnd: Authenticating {username}")
        try:
            # Use filter instead of get to handle duplicate emails
            users = UserModel.objects.filter(email=username)
            if not users.exists():
                print("EmailBackEnd: User not found")
                return None
                
            # If multiple users, try to find one with matching password
            for user in users:
                print(f"EmailBackEnd: Checking user: {user.username}, User type: {user.user_type}")
                if user.check_password(password):
                    print("EmailBackEnd: Password check passed")
                    return user
                else:
                    print(f"EmailBackEnd: Password check failed for user {user.username}")
            
            # If we get here, no user matched the password
            return None
            
        except Exception as e:
            print(f"EmailBackEnd: Error during authentication: {str(e)}")
            return None