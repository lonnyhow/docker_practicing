from ninja import Router
from django.contrib.auth.models import User
from apps.blog_api.schemas.user import UserSchema, UserProfileSchema, UserRegistrationSchema
from ninja_jwt.authentication import JWTAuth
from ninja.errors import ValidationError
from apps.main.models import Post

users_router = Router(tags=['Users'])

@users_router.get('/api/users/all/', response=list[UserSchema])
def get_all_posts(request):
    return User.objects.all()

@users_router.get('/api/users/me', auth=JWTAuth(), response=UserProfileSchema)
def get_user_me(request):
    user = request.user
    return user

@users_router.post('/api/users/', response=UserSchema)
def create_user(request, user_data: UserRegistrationSchema):
    is_username_exists = User.objects.filter(username=user_data.username).exists()
    if is_username_exists:
        raise ValidationError('Username already exists')
    is_email_exists = User.objects.filter(email=user_data.username).exists()
    if is_email_exists:
        raise ValidationError('Email already exists')
    if user_data.password_1 != user_data.password_2:
        raise ValidationError('Passwords do not match')
    user = User.objects.create_user(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password_2,
        first_name=user_data.first_name,
    )
    return user



