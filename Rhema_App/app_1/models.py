from django.db import models

class Book(models.Model):
    Name = models.CharField(max_length=255)
    Old_Test = models.BooleanField(default=False)
    New_Test = models.BooleanField(default=False)
    Gosp = models.BooleanField(default=False)
    Pent = models.BooleanField(default=False)
    num_verses = models.IntegerField(null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # @property
    # def full_name(self):
    #     return self.first_name + ' ' + self.last_name 


class Chapter(models.Model):
    Book = models.CharField(max_length=255) 
    Number = models.IntegerField(null=True)
    num_verses = models.IntegerField(null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # @property
    # def full_name(self):
    #     return self.first_name + ' ' + self.last_name 