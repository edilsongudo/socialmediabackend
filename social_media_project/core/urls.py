from django.urls import path
from .views import postLikeOrDislike, PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', PostViewSet, basename="posts")

urlpatterns = [
    path('like-dislike/<str:id>/',
         postLikeOrDislike, name="post-like-dislike"),
]

urlpatterns += router.urls
