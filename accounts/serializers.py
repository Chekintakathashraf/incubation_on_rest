
from rest_framework import serializers
from accounts . models import CustomUser,Application,Slots
from rest_framework.response import Response
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
            name=self.validated_data['name'],
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
        token['username'] = user.username
        token['applied'] = user.is_staff
        
        return token
  

class ApplicationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Application
        fields = '__all__'

        extra_kwargs = {
            'status' : {'read_only' : True},
        }

        def validate_phone(self,value):
            if len(value)<10 or len(value)>10:
                raise serializers.ValidationError("Phone Number must be 10 characters")
            else:
                return value

class UpdateApplicationStatusSerializer(ApplicationSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class SlotsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Slots
        fields = "__all__"

   
        
        
