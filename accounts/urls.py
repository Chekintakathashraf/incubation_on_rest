
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


    path('addapplication/',views.AddApplication.as_view(),name='addapplication'),
    path('updateapplication/<int:id>/',views.UpdateApplication.as_view(),name='updateapplication'),
    path('getapplications/',views.GetApplicationsView.as_view(),name='getapplications'),
    path('updateapplicationstatus/<int:id>/<int:stid>/',views.UpdateApplicationStatus.as_view(),name='updateapplicationstatus'),

    path('addslots/',views.AddSlots.as_view(),name='addslots'),
    path('updateslot/<int:id>/',views.UpdateSlot.as_view(),name='updateslot'),
    path('getslots/<int:id>/',views.GetSlotsDetailsView.as_view(),name='getslotsdetails'),
    path('getslots/',views.GetSlotsView.as_view(),name='getslots'),
]