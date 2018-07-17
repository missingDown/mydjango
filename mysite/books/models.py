from django.db import models

# Create your models here.
class Publisher(models.Model):
    """创建名为Publisher的数据库表"""
    # 字段名：name 数据类型：varchar 长度：30
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    punlisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()