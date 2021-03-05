from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,default="")
cat=(
    ("Article","1"),
    ("Poem","2")
)
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    author_id=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.CharField(max_length=130)
    views= models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)
    thumbnail = models.ImageField(upload_to='static/img', default="")
    content=models.TextField()
    material=models.TextField()
    category=models.CharField(max_length=14,choices=cat,default="1")

    def __str__(self):
        return self.title + " by " + self.author

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username