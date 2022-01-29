from django.db import models


# Create your models here.
class Exam(models.Model):
    title = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='uploads/')
    short_description = models.CharField(max_length=2400)
    exam_date = models.DateField()
    official_website_link = models.URLField()
    registration_date = models.DateField()
    salary = models.IntegerField()
    vacancies = models.IntegerField()
    official_website_notification = models.FileField(upload_to='uploads/', null=True, blank=True)
    latest_updates_links = models.URLField(null=True, blank=True)
    sts = models.BooleanField(default=True)

    def __str__(self):
        return self.short_description
