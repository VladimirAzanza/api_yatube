from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api_v1'

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='post')
router_v1.register('groups', GroupViewSet, basename='group')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment_post'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
