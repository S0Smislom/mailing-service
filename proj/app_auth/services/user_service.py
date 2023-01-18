from django.contrib.auth.models import User

def create_user(**kwargs):
    return User.objects.create(**kwargs)

def get_user_by_email(email):
    try:
        print('EMAIL', email)
        return User.objects.filter(email=email).first()
    except:
        return None

def create_user(data):
    user =  User.objects.create_superuser(
        username=data.get('email'),
        email = data.get('email'),
        first_name = data.get('first_name'),
        last_name = data.get('last_name'),
        password = '',
    )
    user.set_unusable_password()
    user.save()
    return user