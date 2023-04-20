from rest_framework import status
# 연결상태 전송 헤더
from rest_framework.views import APIView
# API관련 클래스 상속 헤더
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserSerializer,ComtomTokenObtainPairSerializer,UserProfileSerializer
# 사용자 정의 UserSerializer 모델 import
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from .models import User

class UserView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        #serializer를 통한 데이터 저장
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료"},status=status.HTTP_201_CREATED)
        return Response({"message":f"${serializer.errors}"},status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = ComtomTokenObtainPairSerializer


class MockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    #로그인 인증
    def get(self,request):
        return Response("get요청")

class FollowView(APIView):
    def post(self,request,user_id):
        click_user = get_object_or_404(User,id=user_id)
        if request.user in click_user.followers.all():
            click_user.followers.remove(request.user)
            return Response("unfollow", status=status.HTTP_200_OK)
        else:
            click_user.followers.add(request.user)
            return Response("follow", status=status.HTTP_200_OK)

class ProfileView(APIView):
    def get(self,request,user_id):
        user = get_object_or_404(User,id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
