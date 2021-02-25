from django.urls import path, re_path
from users import views

urlpatterns = [
    re_path(r'^signup(?:(?P<error>\w+)/)?$', views.sign_up_page, name="Sign Up Page"),
    path('register', views.sign_up, name="Sign Up")
]