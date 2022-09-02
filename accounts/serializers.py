from rest_framework import serializers
from accounts . models import CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["name","username","email","password"]  

        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    
    def validate_password(self,value):
        if len(value)<4:
            raise serializers.ValidationError("Password must be minimum 4 characters")
        else:
            return value
    def save(self):
        reg = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        reg.set_password(password)
        reg.save()
        return reg

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        
        return token

