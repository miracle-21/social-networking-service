from django.db import models

from core.models import TimeStampModel

class Post(TimeStampModel):
    title   = models.CharField(max_length=50)
    image   = models.ImageField(null=True)
    content = models.TextField()
    like    = models.PositiveSmallIntegerField(default=0) # Values from 0 to 32767

    class Meta:
        db_table = 'posts'
        ordering = ('update_at')

    def __str__(self):
        return self.title


class Comment(TimeStampModel):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    @property # 필드 접근 방법 변경
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content