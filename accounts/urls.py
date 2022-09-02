
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView

urlpatterns = [
    path('register/',views.Register.as_view(),name='register'),

    path('token/create/', views.MyTokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]