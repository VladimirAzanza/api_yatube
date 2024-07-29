from rest_framework import serializers

from posts.models import Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)
