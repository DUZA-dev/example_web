from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.views import CreateUserAPIView

urlpatterns = [
    path('sign_up/', CreateUserAPIView.as_view({'post': 'create'})),
    path('sign_in/', TokenObtainPairView.as_view()),

    path('refresh/', TokenRefreshView.as_view()),
]
