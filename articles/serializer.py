from rest_framework import serializers
from .models import Article,Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self,obj):
        return obj.user.email
    class Meta:
        model = Comment
        exclude = ("article",)

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_set = CommentSerializer(many=True)
    likes = serializers.StringRelatedField(many=True)
    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Article
        fields = "__all__"

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title","image","content")


class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_user(self,obj):
        return obj.user.email
    # 약속된 형태, 메소드 필드를 받고, get_user를 사용하여 user의 email 값을 반환받는다.
    def get_likes_count(self,obj):
        return obj.likes.count()
    def get_comments_count(self,obj):
        return obj.comment_set.count()


    class Meta:
        model = Article
        fields = ("pk","title","image","updated_at","user","likes_count","comments_count")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)