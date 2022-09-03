

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from accounts.models import CustomUser,Application
from accounts.serializers import UserSerializer,MyTokenObtainPairSerializer,ApplicationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView



# Create your views here.
class UserRegister(APIView):
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


class GetUserDetailsView(APIView):
    # permission_classes=[IsAdminUser]
    serializer_classes = UserSerializer
    def get(self, request,id):
        try:
            user = CustomUser.objects.get(id=id)
            serializer = UserSerializer(user,many=False)   
            return Response(serializer.data)
        except:
            message = {'message':'No User with this id already exist'}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

class GetUsersView(APIView):
    permission_classes=[IsAdminUser]
    serializer_classes = UserSerializer
    def get(self, request):
    
        users = CustomUser.objects.all()
        serializer = UserSerializer(users,many=True)   
        return Response(serializer.data)


class AddApplication(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors)

class UpdateApplication(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request,id):
        details = Application.objects.get(id=id)
        serializer = ApplicationSerializer(details,context={'request': request})
        return Response(serializer.data)
    def put(self, request,id):
        print(request.body)
        details = Application.objects.get(id=id)
        serializer = ApplicationSerializer(details,data=request.data,)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update application successfully updated")
            return Response(serializer.data)
        else:
            print("Update application failed")
            return Response(serializer.errors)    
    def delete(self, request,id):
        details = Application.objects.get(id=id)
        details.delete()
        return Response({'message':'Application deleted'})
    def patch(self, request,id):
        details = Application.objects.get(id=id)
        serializer = ApplicationSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            print("Update application successfully updated")
            return Response(serializer.data)
        else:
            print("Update application failed")
            print(serializer.errors)
            return Response(serializer.errors)


class GetApplicationsView(APIView):
    permission_classes=[IsAdminUser]
    serializer_classes = ApplicationSerializer
    def get(self, request):
    
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications,many=True)   
        return Response(serializer.data)