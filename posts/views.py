import imp
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from posts.models import Post, Comment
from posts.serializers import PostListSerializer, CreateSerializer, CommentSerializer, PostSerializerDetail

class PostPageNumberPagination(PageNumberPagination):
    page_size = 10 # 페이지 당 디폴트 게시글 수 10개
    page_size_query_param = 'page_size' # 페이지 당 게시글 수를 조정

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination

    '''
    게시물 조회
    '''
    def view(self, request, *args, **kwargs):
        instance = self.get_object() # DB에서 인스턴스 꺼내기
        instance.view += 1 # 조회 시마다 조회수 +1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CreateViewSet(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreateSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#     # ViewSet에서는 get 메서드를 사용하지 않아서 like로 변경
#     def like(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.like += 1
#         instance.save()

#         return Response(instance.like)

class PostRetrieveListAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerDetail

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        commentList = instance.comment_set.all()
        data = {
            'post': instance,
            'commentList' : commentList,

        }
        serializer = self.get_serializer(instance = data)
        return Response(serializer.data)