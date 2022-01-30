from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import PostViewSet, postLikeOrDislike


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('', include(router.urls)),
    path('post-like-or-dislike/<str:id>/', postLikeOrDislike, name="post-like-dislike"),
]
