from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers

from api.views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
# Не знаю, использовать ли регулярное выражение для урл или
# библиотеку rest_framework_nested.routers, чтобы сократить код.

router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment_post'
)

# comment_router = routers.NestedSimpleRouter(
#    router,
#    r'posts',
#    lookup='post'
# )
# comment_router.register(r'comments', CommentViewSet, basename='comment-post')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    # path('', include(comment_router.urls))
]
