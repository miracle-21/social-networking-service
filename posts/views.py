from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from posts.models import Post, Comment
from posts.serializers import PostListSerializer, CreateSerializer, CommentSerializer, PostDetailSerializer


class PostPageNumberPagination(PageNumberPagination):
    '''
    페이지네이션
    '''
    page_size = 10 # 페이지 당 디폴트 게시글 수 10개
    page_size_query_param = 'page_size' # 페이지 당 게시글 수를 조정

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination

    '''
    메인페이지
    '''

class PostDetailListAPIView(RetrieveUpdateDestroyAPIView):
    '''
    상세페이지 조회/수정/삭제
    '''
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view += 1 # 조회 시마다 조회수 +1
        instance.save()
        commentList = instance.comment_set.all()
        data = {
            'post': instance,
            'commentList' : commentList,

        }
        serializer = self.get_serializer(instance = data)
        return Response(serializer.data)

class CreateViewSet(CreateAPIView):
    '''
    게시물 생성
    '''
    queryset = Post.objects.all()
    serializer_class = CreateSerializer

class PostLikeAPIView(GenericAPIView):
    queryset = Post.objects.all()
    '''
    좋아요 기능
    NOTICE: 한 사람당 좋아요 개수 제한이 없다. 좋아요 취소는 안된다.
    '''
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()

        return Response(instance.like)

class CommentCreateAPIView(CreateAPIView):
    '''
    댓글 
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdateAPIView(RetrieveUpdateDestroyAPIView):
    '''
    댓글 수정/삭제
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

