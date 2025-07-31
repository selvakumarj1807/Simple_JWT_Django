from django.urls import path
from .views import RegisterView, UserListView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_page, login_page, accounts_page, logout_page

urlpatterns = [
    # HTML templates
    # HTML Pages
    path('register-page/', register_page),
    path('login-page/', login_page),
    path('accounts-page/', accounts_page),
    path('logout-page/', logout_page),
    
    # API endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', UserListView.as_view(), name='view_accounts'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
