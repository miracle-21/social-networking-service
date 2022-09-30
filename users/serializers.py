from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8,write_only=True) # write_only 사용하면 get으로도 확인 안됨
    
    class Meta:
        model  = User
        fields = ['username', 'email', 'password', 'is_staff']

    def create(self, validated_data):
        '''
        회원가입
        '''
        user = User.objects.create_user(
            username = validated_data['username'],
            email    = validated_data['email'],
            password = validated_data['password'],
        )
        return user
    
    def destroy(self, request):
        '''
        회원탈퇴
        '''
        user = self.get_object()
        user.delete()