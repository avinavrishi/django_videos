from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
POST_CATEGORY= (

    ('AMATEUR', 'amateur'),
    ('ANAL', 'anal'),
     ('ASIAN', 'asian'),
     ('BDSM', 'bdsm'),
    ('BLONDE', 'blonde'),
    ('BRUNETTE', 'brunette'),
     ('CREAMPIE', 'creampie'),
     ('CUMSHOT', 'cumshot'),
     ('FISTING', 'fisting'),
    ('GANGBANG', 'gangbang'),
       ('GERMAN','german'),
     ('INDIAN', 'indian'),
        ('LATINA', 'latina'),
        ('LESBIAN', 'lesbian'),
        ('MILF','milf'),
        ('REDHEAD', 'redhead'),
        ('SOLO', 'solo'),
        ('SQUIRTING', 'squirting'),
        ('TEEN', 'teen'),

    )
 
class Post(models.Model):
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    imagefile = models.ImageField(upload_to = 'images/' , null = True, verbose_name = "")
    videofile = models.FileField(upload_to = 'videos/' , null = True, verbose_name = "")
    Post_category = models.CharField(max_length=10, choices = POST_CATEGORY, default="")
    updated_on = models.DateTimeField(auto_now= True)
    keywords = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
   

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)