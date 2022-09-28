from django.urls import path

from posts.views import PostViewSet

urlpatterns = [
    path('', PostViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path('<int:pk>/', PostViewSet.as_view(actions={'get': 'view','patch': 'partial_update', 'delete': 'destroy'})),
]