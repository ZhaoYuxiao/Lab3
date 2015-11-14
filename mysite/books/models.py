from django.db import models
    
        
class Author(models.Model):
    authorid = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
        
        
class Book(models.Model):
    isbn = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=100)
    authorid = models.ForeignKey(Author)
    publisher = models.CharField(max_length=30)
    publishDate = models.CharField(max_length=30)
    price = models.FloatField() 
    
    def __unicode__(self):
        return self.title