from django.db import models

from core.models import TimeStampModel

# 회원 테이블
class User(TimeStampModel):
    name      = models.CharField(max_length = 30)
    nickname  = models.CharField(max_length = 30, unique = True)
    email     = models.CharField(max_length = 255, unique = True)
    password  = models.CharField(max_length = 100)

    class Meta():
        db_table = 'users'

    def __str__(self):
        return self.name