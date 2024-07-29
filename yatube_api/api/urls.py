from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet

app_name = 'api'
router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls))
]
