from django.db import models

# Create your models here.
class subject(models.Model):
    subject_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.subject_name