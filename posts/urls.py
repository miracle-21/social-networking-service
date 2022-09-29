from django.urls import path

from posts.views import *

urlpatterns = [
    path('', PostViewSet.as_view(actions={'get': 'list'})), # 메인페이지
    path('<int:pk>/', PostRetrieveListAPIView.as_view()),
    path('board/', CreateViewSet.as_view()), # 게시글 작성 페이지
    path('comment/', CommentCreateAPIView.as_view()), # 댓글 생성
    path('comment/<int:pk>/', CommentUpdateAPIView.as_view()), # 댓글 수정/삭제
    path('<int:pk>/like/', PostLikeAPIView.as_view()),
] 