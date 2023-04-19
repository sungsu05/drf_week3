from rest_framework import status
# 연결상태 전송 헤더
from rest_framework.views import APIView
# API관련 클래스 상속 헤더
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import UserSerializer,ComtomTokenObtainPairSerializer
# 사용자 정의 UserSerializer 모델 import
from rest_framework import permissions

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