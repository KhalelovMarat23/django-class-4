from django.urls import path
from users import views

urlpatterns = [
    path('signup', views.sign_up_page, name="Sign Up Page"),
    path('register', views.sign_up, name="Sign Up")
]