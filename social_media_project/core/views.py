from django.shortcuts import redirect
from .models import Post
from django.contrib.auth.models import User
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied, NotAuthenticated


# # ViewSets define the view behavior.
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly,
#         IsOwnerOrReadOnly
#     ]


@api_view(['GET'])
def apiOverview(request):
    return redirect('schema-swagger-ui')


@api_view(['GET'])
def postList(request):
    posts = Post.objects.all().order_by('-id')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postByUserList(request, pk):
    author = User.objects.get(id=pk)
    posts = Post.objects.filter(author=author).order_by('-id')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postDetail(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)

    if not request.user.is_authenticated:
        raise NotAuthenticated()

    if serializer.is_valid():
        serializer.save(author=request.user)

    return Response(serializer.data)


@api_view(['POST'])
def postUpdate(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if not request.user.is_authenticated:
        raise NotAuthenticated()

    if post.author != request.user:
        raise PermissionDenied()

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def postDelete(request, pk):
    post = Post.objects.get(id=pk)

    if not request.user.is_authenticated:
        raise NotAuthenticated()

    if post.author != request.user:
        raise PermissionDenied()

    post.delete()

    return Response('Item succsesfully delete!')


@api_view(['GET'])
def postLikeOrDislike(request, id):
    post = Post.objects.get(id=id)

    if not request.user.is_authenticated:
        raise NotAuthenticated()

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        print('Dislike')
        return Response({"details": "disliked"})
    else:
        post.likes.add(request.user)
        print('like')
        return Response({"details": "liked"})
