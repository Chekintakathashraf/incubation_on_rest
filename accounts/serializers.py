
from rest_framework import serializers
from accounts . models import CustomUser,Application
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
    # print("qqqqqqqqqqqqqqqqqqqqqqqqqqqq")



    # def cookies(token):
            
    #     response = Response()
    #     response.set_cookie(key='refresh_token',value=token,httponly=True)
    #     response.data = {
    #     'refresh_token' : token
    #     }
    #     print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    #     print(response)
    #     return response
    # token = get_token(cls, user)
    # cookies(token)
# token = MyTokenObtainPairSerializer.get_token()
# cookie = MyTokenObtainPairSerializer.cookies(token)

    

class ApplicationSerializer(serializers.ModelSerializer):
     class Meta:
        model = Application
        fields = '__all__'