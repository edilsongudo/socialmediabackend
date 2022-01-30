from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]


@api_view(['GET'])
def postLikeOrDislike(request, id):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data['user']
    post = Post.objects.get(id=id)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        print('Dislike')
        return Response({'details': 'disliked'})
    else:
        post.likes.add(request.user)
        print('like')
        return Response({'details': 'liked'})

