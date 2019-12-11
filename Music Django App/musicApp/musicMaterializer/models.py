from django.db import models

# pip install django-multiselectfield
# from multiselectfield import MultiSelectField


class FileModel(models.Model):
    title = models.CharField(max_length=100)
    apikey = models.CharField(max_length=500)
    file = models.FileField(upload_to='files')


    def __str__(self):
        return self.title


