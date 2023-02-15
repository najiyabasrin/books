from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

books=[

    {"id":1,"bookname":"cleopatra","author":"shekspiere","price":100},
    {"id":2,"bookname":"hxbsjcb","author":"xcxxc","price":200},
    {"id":3,"bookname":"bhdbdsjdhsj","author":"sxccc","price":300},
    {"id":4,"bookname":"hxbsxbnc","author":"cdcmhsh","price":400},
    {"id":5,"bookname":"sxcnjcbbn","author":"xcbchhdh","price":500}
]

class Books(models.Model):
    bookname=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self):
        return self.bookname