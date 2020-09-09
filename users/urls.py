from django.urls import path
from . import views as user_views

app_name = "users"

urlpatterns = [path("", user_views.all_users, name="users")]
