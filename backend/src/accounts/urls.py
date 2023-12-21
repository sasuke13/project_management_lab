from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, CreateSuperuserView, UpdateUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_superuser/', CreateSuperuserView.as_view(), name='create-superuser'),
    path('update_user/', UpdateUserView.as_view(), name='update-user'),
]
