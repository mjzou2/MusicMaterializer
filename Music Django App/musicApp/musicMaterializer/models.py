from django.db import models

# pip install django-multiselectfield
# from multiselectfield import MultiSelectField


class FileModel(models.Model):
    title = models.CharField(max_length=100)
    apikey = models.CharField(max_length=100)
    file = models.FileField(upload_to='files')

    # MY_CHOICES = (('Detect BPM', 'Detect BPM')
    #               ('Record', 'Record'))

    # my_field = MultiSelectField(choices=MY_CHOICES)
    detect_bpm = models.BooleanField('Detect BPM', default=False)
    record = models.BooleanField('Record Audio', default = False)


    def __str__(self):
        return self.title


