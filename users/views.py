from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    회원가입/탈퇴 view
    '''
    permission_classes = [AllowAny]

    queryset = User.objects.all()
    serializer_class = UserSerializer
