from unicodedata import category
from django.db import models
import datetime
import os
from autoslug import AutoSlugField
from matplotlib.pyplot import title



def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('static/postimage', filename)



class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title = models.TextField(max_length=191)
    Category = models.TextField(max_length=500, null=True)
    content=models.TextField()
    description =models.TextField(max_length=291)
    keywords = models.TextField(max_length=291)
    slug= AutoSlugField(populate_from='title',unique=True)
    timeStamp=models.DateTimeField(blank=True)
    author=models.CharField(max_length=14)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)

    
        

   
    
    

  

