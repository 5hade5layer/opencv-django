from django.db import models
from django.conf import settings
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ("input", ext)
    os.remove(os.path.join(settings.MEDIA_ROOT, ""+filename))
    return os.path.join(instance.directory_string_var, filename)
class Simulation(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to=get_file_path)
    directory_string_var = ''
    def __str__(self):
        return self.title


    