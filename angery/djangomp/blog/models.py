from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, primary_key= True)
    def __str__(self):
        return 'Author: {} {}'.format(self.last_name,self.first_name)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    cdate = models.DateTimeField(editable=False)
    edate = models.DateTimeField()
    title = models.CharField(max_length = 100)
    content = models.TextField()
    def __str__(self):
        return 'Author: {} {}'.format(self.author,self.title)

class Comments(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Ppost = models.ForeignKey(Post, on_delete=models.CASCADE)
    cdate = models.DateTimeField(editable=False)
    content = models.TextField()

    def __str__(self):
        return 'Comment # {}'.format(self.id)