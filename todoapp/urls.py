from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("delete/<int:id>/",views.delete,name='delete'),
    path("login/",views.login_view,name="login"),
    path("signup/",views.signup_view,name="signup"),
    path("logout/",views.logout_view,name="logout"),
]