
from django.db import models

# Create your models here.

class categories(models.Model):
  
    title = models.CharField(max_length = 200)
    description = models.TextField()
    no_of_vacancy = models.IntegerField()
    image = models.ImageField()

    def _str_(self):
        return self.title

class jobdescrip(models.Model):
   
    title = models.CharField(max_length = 200)
    description = models.TextField()
    no_of_vacancy = models.IntegerField()
    image = models.ImageField()
    experience = models.TextField()
    documents = models.TextField()
    skill = models.TextField()
    language  = models.TextField()
    salary = models.TextField()
    age = models.TextField()
    Category = models.ForeignKey('categories', on_delete=models.CASCADE)


    def _str_(self):
        return self.title




    




