from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'contact'
