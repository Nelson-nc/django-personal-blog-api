from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('logout/', views.LogoutApiView.as_view(), name="logout"),
    path('register/', views.RegisterApiView.as_view(), name="register"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]
