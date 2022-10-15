from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOISES  = (
        (-1, "Default"),
        (0, "Running"),
        (1, "Completed"),
        (2,"Error"))
    status=models.IntegerField(blank=True, null=True, default=-1, choices=STATUS_CHOISES)
    # pid = models.IntegerField(blank=True, null=True, default=0)
    swagger_file = models.FileField("", upload_to="media", max_length=1024)
    result_dir = models.FilePathField("",
                                      path="media",
                                      match=None,
                                      recursive=False,
                                      max_length=1024,
                                      blank=True,
                                      null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)