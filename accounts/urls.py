from django.urls import path, include
from .views import UserRegister, UserLogin, UserLogout, UserDashboard
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'accounts'

api_views = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('dashboard/<str:username>/', UserDashboard.as_view(), name='dashboard'),
    path('api/', include(api_views))
]