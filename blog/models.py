from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    uploaded_file = models.FileField(upload_to='images/')
    expiration_date = models.DateField()
    expired = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.id)} {self.expired}"