from django.urls import path

from posts.views import PostViewSet, CreateViewSet

urlpatterns = [
    path('', PostViewSet.as_view(actions={'get': 'list'})), # 메인페이지
    path('board/', CreateViewSet.as_view()), # 게시글 작성 페이지
    path('<int:pk>/', PostViewSet.as_view(actions={'get': 'view','patch': 'partial_update', 'delete': 'destroy'})), # 상세페이지
] 