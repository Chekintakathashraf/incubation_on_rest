
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('register/',views.UserRegister.as_view(),name='register'),
    path('getuser/<int:id>',views.GetUserDetailsView.as_view(),name='getuserdetails'),
    path('getusers/',views.GetUsersView.as_view(),name='getusers'),
    

    path('token/create/', views.MyTokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]