from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
# from core.views import PostViewSet, postLikeOrDislike
from core.views import (
    postList,
    postByUserList,
    postDetail,
    postCreate,
    postDelete,
    postUpdate,
    postLikeOrDislike,
    apiOverview)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    # path('', include(router.urls)),
    path('', apiOverview, name="api-overview"),
    path('post-list/', postList, name="post-list"),
    path('post-by-user-list/<str:pk>/', postByUserList, name="post-by-user-list"),
    path('post-detail/<str:pk>/', postDetail, name="post-detail"),
    path('post-create/', postCreate, name="post-create"),
    path('post-update/<str:pk>/', postUpdate, name="post-update"),
    path('post-delete/<str:pk>/', postDelete, name="post-delete"),
    path('post-like-or-dislike/<str:id>/',
         postLikeOrDislike, name="post-like-dislike"),
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),
]
