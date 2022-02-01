from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'
        # depth = 1
        read_only_fields = ['author']

    def create(self, validated_data):
        post = Post.objects.create(
            title=validated_data['title'],
            content=validated_data['content'],
            author=self.context['request'].user,
        )
        return post
