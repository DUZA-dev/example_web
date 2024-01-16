from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.models import User
from core.serializers import UserSerializer



class CreateUserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

