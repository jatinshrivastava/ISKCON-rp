from itsdangerous import URLSafeTimedSerializer
from decouple import config

SECRET_KEY = config('SECRET_KEY')
SECURITY_PASSWORD_SALT = config('SECURITY_PASSWORD_SALT')


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(email, salt=SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(SECURITY_PASSWORD_SALT)
    try:
        email = serializer.loads(
            token,
            salt=SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
    except:
        return False
    return email