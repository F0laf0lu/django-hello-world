from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework_simplejwt import views

urlpatterns = [
    # path("accounts/", include("djoser.urls"))

    # Authentication
    path("auth/create", views.TokenObtainPairView.as_view(), name="jwt-create"),
    path("auth/refresh", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    path("auth/verify", views.TokenVerifyView.as_view(), name="jwt-verify"),

    # Accounts
    path('accounts/register/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
]
