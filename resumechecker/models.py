from django.db import models

class Resume(models.Model):
    resume=models.FileField(upload_to="resume/")

class Jobs(models.Model):
    job_title=models.CharField(max_length=100)
    job_description=models.TextField()

    def __str__(self):
        return self.job_title 
# Create your models here.
