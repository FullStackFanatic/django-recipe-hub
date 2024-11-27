from django.db import models

# Create your models here.
# crud

# class Student(models.Model):
#     # id = models.AutoField()
#     name = models.CharField(max_length=100) 
#     address = models.TextField(null=True,blank = True)
#     age = models.IntegerField()
#     email = models.TextField(null=True,blank = True)


#     def __str__(self) -> str:
#        return self.name

class Student(models.Model):
    # id = models.AutoField()  # This is implicit and can be omitted.
    name = models.CharField(max_length=100) 
    address = models.TextField(null=True, blank=True)
    age = models.IntegerField()
    email = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
