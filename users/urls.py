from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, ProfilePasswordRestoreView, confirm_user

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/user_login.html'), name='login'),
    path("registration/", RegisterView.as_view(), name="registration"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('restore_password/', ProfilePasswordRestoreView.as_view(), name="restore_password"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('confirm/<str:code>/', confirm_user, name="confirm")
]