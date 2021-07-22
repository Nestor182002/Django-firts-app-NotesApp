from django.db import models

# usuarios de django
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.



class PostsModels(models.Model):
     userforeign = models.ForeignKey(User, on_delete=models.CASCADE)
     title=models.CharField(max_length=50,null=True)
     problem=models.CharField(max_length=250,null=False)
     solution=models.CharField(max_length=250,null=False)

     def __str__(self):
        return self.title    

     class Meta:
        ordering = ["-pk",]

   


class ComentPosts(models.Model):
   postforeign=models.ForeignKey(PostsModels,on_delete=models.CASCADE)
   usercoment = models.ForeignKey(User, on_delete=models.CASCADE)
   comentario=models.CharField(max_length = 150)

   def get_absolute_url(self):
        url=reverse('detail-post', kwargs={"pk":self.postforeign.id})
        return url

   def __str__(self):
        return self.comentario 


   








    



        

