from django.db import models
from django.contrib.auth.models import User

from PIL import Image

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

STAGE = (
    ('Planning', "Planning"),
    ('Execution', "Execution"),
    ('Optimization', "Optimization")
)

TYPE = (
    ('post', "post"),
    ('page', "page"),
    ('case_studies', "case_studies"),
    ('featured','featured')
)


class Department (models.Model):
    name = models.CharField(max_length=200, unique=True)
    sales_point = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Industry (models.Model):
    name = models.CharField(max_length=200, unique=True)
    focus = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    post_image = models.ImageField(
        upload_to='post/', default='img/post/personal.png')
    post_image_alt = models.CharField(max_length=200, blank=True,
                                      null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='department_post', blank=True,
                                   null=True,)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, null = True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    focus = models.TextField(blank=True,null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    stage = models.CharField(max_length=400, choices=STAGE, blank=True,
                             null=True)
    type = models.CharField(max_length=400, choices=TYPE,  blank=True,
                             null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
