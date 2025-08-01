from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


# API Views
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # Requires blacklist app
            return Response({"detail": "Logged out"}, status=205)
        except Exception as e:
            return Response({"error": str(e)}, status=400)



# HTML views
from django.shortcuts import render

def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

def accounts_page(request):
    return render(request, 'accounts.html')

def logout_page(request):
    return render(request, 'logout.html')
