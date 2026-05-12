from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import SignupSerializer
from django.http import HttpResponse
from .serializers import UserSerializer
# Create your views here.
"""
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message':'hello'}
        return Response(content)
"""


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protectedProfile(request):

    serializer = UserSerializer(request.user)

    return Response({"username": request.user.username,"message":"Protected API working"})






@api_view(['POST'])
def signup(request):
    serializer_signup = SignupSerializer(data=request.data)

    if serializer_signup.is_valid():
        serializer_signup.save()

        return Response({"message":"User Created"})
    return Response(serializer_signup.errors,status=400)



"""
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'User already exists'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return Response({'message': 'User created successfully'})
"""