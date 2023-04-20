from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from articles.serializer import ArticleListSerializer
from .models import User


class UserProfileSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    article_set = ArticleListSerializer(many=True)
    like_articles = ArticleListSerializer(many=True)

    class Meta:
        model = User
        fields = ("id","email","followings","followers","article_set","like_articles")



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        # 부모 클래스의 create메서드를 호출, 인자값을 전달하고 반환값을 user 변수에 담는다.
        password = user.password
        user.set_password(password)
        # 비밀번호 복호화
        user.save()
        return user
    def update(self, instance, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

class ComtomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token