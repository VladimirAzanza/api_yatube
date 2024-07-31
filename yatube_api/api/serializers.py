from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GetAuthorInfoSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username


class CommentSerializer(GetAuthorInfoSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class PostSerializer(GetAuthorInfoSerializer):
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=False
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author', 'pub_date')
