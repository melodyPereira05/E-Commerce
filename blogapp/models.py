# from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator

post_list = User.objects.all()
paginator = Paginator(post_list, 5)

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


BLOG_CATEGORY = (
    (0, 'None'),
    (1, 'Creative'),
    (2, 'Design'),
    (3, 'News'),
    (4, 'Photography'),
    (5, 'Corporate'),
)

class BlogModel(models.Model):
    id = models.IntegerField(primary_key=True)
    blog_title = models.CharField(max_length=100)
    # title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    # content = models.TextField()
    # content2 = models.TextField(null = True)
    # quote = models.CharField(max_length=200, default="Always deliver more than expected.")
    # quote_by = models.CharField(max_length=50, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category1 = models.IntegerField(choices=BLOG_CATEGORY, default=0)
    about_keyword1 = models.CharField(max_length=20, null=True)
    about_keyword2 = models.CharField(max_length=20, null=True)
    about_keyword3 = models.CharField(max_length=20, null=True)
    blog = models.TextField()

    def datepublished(self):
        return self.created_on.strftime('%B %d %Y')
 
    def __str__(self):
        return f"Blog: {self.blog_title}"
 
class CommentModel(models.Model):
    your_name = models.CharField(max_length=20)
    # email = models.EmailField()
    comment_text = models.TextField()
    blog = models.ForeignKey('BlogModel', on_delete=models.CASCADE)
     
    def __str__(self):
        return f"Comment by Name: {self.your_name}"

