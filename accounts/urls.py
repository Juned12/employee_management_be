from django.urls import path
from .views import ManagerView, RegisterView, EmployeeView, CreateEmployeeView, ListEmployeeView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('me/', ManagerView.as_view()),
    path('auth/register/', RegisterView.as_view()),
    path('employee/create/', CreateEmployeeView.as_view()),
    path('employee/<int:pk>/', EmployeeView.as_view()),
    path('employees/', ListEmployeeView.as_view()),

]