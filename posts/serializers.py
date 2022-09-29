from rest_framework import serializers

from posts.models import Post, Tag


class PostListSerializer(serializers.ModelSerializer):
    like = serializers.IntegerField(default=0, read_only=True)
    view = serializers.IntegerField(default=0, read_only=True)
    tag = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        ordering = ['-id']
        fields = '__all__'
        
class CreateSerializer(serializers.ModelSerializer):
    '''
    게시물 생성
    NOTICE: tag 값이 None으로 나온다.
    '''
    like = serializers.IntegerField(default=0, read_only=True)
    view = serializers.IntegerField(default=0, read_only=True)
    tag = serializers.CharField()
    image = serializers.ImageField(use_url=True, default=None)

    class Meta:
        model = Post
        fields = '__all__'
   
    # 게시물 작성
    def create(self, validated_data):
        if 'image' in validated_data.keys():
            p1 = Post(
                title = validated_data['title'],
                content = validated_data['content'],
                image = validated_data['image']
            )
        else:
            p1 = Post(
                title = validated_data['title'],
                content = validated_data['content']
            )
        p1.save()
        tag_data = validated_data['tag']
        result = 'True'
        # for key, value in tag.items():
        for v in tag_data.split(','):
            if v.startswith('#'):
                for i in Tag.objects.all():
                    if v == i.name:
                        p1.tag.add(i)
                        p1.save()
                        result = 'False'
                        break
                if result =='False':
                    result = 'True'
                    continue
                t1 = Tag(name=v)
                t1.save()
                p1.tag.add(t1)
                p1.save()
        return p1

        # t1 = Tag(validated_data['tag'])
        # t1.save()
        # p1 = Post(
        #     title = validated_data['title'],
        #     content = validated_data['content']
        # )
        # p1.save()
        # p1.tag.add(t1)
        # p1.save()
        # return p1
 


# class PostRetrieveSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     tags = serializers.StringRelatedField(many=True)
    
#     class Meta:
#         model = Post
#         fields = '__all__'  

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'