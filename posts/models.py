from django.db import models

from core.models import TimeStampModel

class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name

class Post(TimeStampModel):
    tag     = models.ManyToManyField(Tag, related_name='post_tags')
    title   = models.CharField(max_length=50)
    image   = models.ImageField(upload_to="%Y/%m/%d", null=True)
    content = models.TextField()
    like    = models.PositiveSmallIntegerField(default=0) # Values from 0 to 32767
    view    = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['-id']
        db_table = 'posts'

    def __str__(self):
        tag = ','.join(str(v) for v in self.tag.all())
        # return self.title
        return "{},{},{}".format(self.title, self.content, tag)


class Comment(TimeStampModel):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        db_table = 'comments'

    @property # 필드 접근 방법 변경
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content