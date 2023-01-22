from django.urls import path
# from .views import AjaxHandler
from base.views import create_user
from base.views import check_login

urlpatterns= [
    # path('', views.home, AjaxHandler.as_view() name="home"),
    path('login/', check_login),
    path('signup/', create_user),
    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    # path('signup/', views.signup, name="signup"),
]