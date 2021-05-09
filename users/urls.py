from django.urls import path
from users import views as core_views
from users.forms import UserLoginForm
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
            'login/',
            views.LoginView.as_view(
                template_name="registration/login.html",
                authentication_form=UserLoginForm
                ),
            name='login'
    ),
    # path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="chapter_index.html"), name='logout'),
    path('signup/', core_views.signup, name='signup'),
]

# path("logout/", auth_views.auth_logout, name='logout'),
# path("", auth_views.LogoutView.as_view(LOGOUT_REDIRECT_URL='chapter_index'), name='logout'),