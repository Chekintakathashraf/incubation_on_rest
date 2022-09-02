from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from accounts.serializers import UserSerializer,MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class Register(APIView):
    permission_classes=[AllowAny]
    serializer_classes = UserSerializer
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_classes(data=data)

        if serializer.is_valid():
            serializer.save()

            response={
                "messages" : "User Created Successfully",
                "data" : serializer.data
            }

            return Response(data= response, status = status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

