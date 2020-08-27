from django.urls import path

from . import views
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, \
    CreateProfilePageView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit/profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('passord/success/', views.password_success, name='password_success'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile'),
    path('edit/profile/page/<int:pk>', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create/profile/page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]
