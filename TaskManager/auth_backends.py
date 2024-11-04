from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class UserIDBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to find user by user_id (assuming user_id is an integer)
            user_id = int(username)
            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, ValueError):
            # If not found, fall back to the default behavior
            user = super().authenticate(request, username, password, **kwargs)

        if user is not None and user.check_password(password):
            return user
        return None
