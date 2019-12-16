from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from mdeditor.fields import MDTextField


# from mysite.settings import AUTH_USER_MODEL


# Create your models here.

class User(AbstractUser):
    class Meta:
        abstract = False


class Common(models.Model):
    """
    common model
    """
    create_user = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_create_user', db_index=False,
                                    on_delete=models.SET_NULL, verbose_name='创建人', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True, blank=True)
    write_user = models.ForeignKey(User, verbose_name='修改人', on_delete=models.SET_NULL, null=True, blank=True,
                                   db_index=False, related_name='%(app_label)s_%(class)s_write_user')
    write_date = models.DateTimeField(verbose_name='修改时间', auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Catalog(Common):
    name = models.CharField(max_length=200)
    name_eng = models.CharField(max_length=200)
    order_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'blog_catalog'
        ordering = ["-order_id", "-id"]
        verbose_name_plural = _(u"分类")
        app_label = 'blog'

    def __str__(self):
        return self.name_eng + '-' + self.name

    def __repr__(self):
        return self.name_eng


class Tag(Common):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'blog_tag'
        ordering = ["-id"]
        verbose_name_plural = _(u"标签")
        app_label = 'blog'

    def __str__(self):
        return self.name


class Link(Common):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    order_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'blog_link'
        ordering = ["-order_id", "-id"]
        verbose_name_plural = _(u"链接")
        app_label = 'blog'

    def __str__(self):
        return self.name


class Articles(Common):
    name = models.CharField(max_length=200, verbose_name='标题')
    # body = models.TextField('内容')
    body = MDTextField('内容')
    visited = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='blog/static/blog/uploads', null=True, blank=True)
    catalog = models.ForeignKey(Catalog, related_name='articles', on_delete=models.SET_NULL,
                                null=True, blank=True, db_index=False)
    recommand = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    order_id = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, through='Articleship', through_fields=('article', 'tag'))

    def image_data(self):
        print(self.photo.url)
        return format_html(
            '<img src="{}" width="100px"/>',
            self.photo.url if self.photo else None,
        )

    image_data.short_description = '图片'

    class Meta:
        db_table = 'blog_article'
        ordering = ["-order_id", "-id"]
        verbose_name_plural = _("文章")
        app_label = 'blog'

    def __str__(self):
        return self.name


class Articleship(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, db_index=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, db_index=False)

    class Meta:
        db_table = 'blog_article_tag'
        app_label = 'blog'


class Comment(Common):
    body = models.TextField()
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    article = models.ForeignKey(Articles,
                                related_name='comments',
                                related_query_name='comment',
                                on_delete=models.CASCADE,
                                db_index=False)

    class Meta:
        db_table = 'blog_comment'
        ordering = ["-id"]
        verbose_name_plural = _(u"评论")
        app_label = 'blog'

    def __str__(self):
        return str(self.id) + '--' + self.article.name


class SinaStock(Common):
    name = models.CharField(max_length=50, db_index=True)
    price = models.FloatField()
    rate = models.FloatField()
    range = models.FloatField()
    quantity = models.FloatField()
    amount = models.FloatField()

    class Meta:
        db_table = 'blog_stock'
        ordering = ["-id"]
        verbose_name_plural = _(u"大盘指数")
        app_label = 'blog'

    def __str__(self):
        return str(self.id) + '--' + self.name


class SinaFutures(Common):
    name = models.CharField(max_length=50, db_index=True)
    price = models.FloatField()

    class Meta:
        db_table = 'blog_future'
        ordering = ["-id"]
        verbose_name_plural = _(u"期货指数")
        app_label = 'blog'

    def __str__(self):
        return str(self.id) + '--' + self.name
