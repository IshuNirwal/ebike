from django.db import models

# Create your models here.


class DealerEnquiry(models.Model):
    name=models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField()
    state=models.CharField(max_length=100)
    business=models.CharField(max_length=1000)
    firm_name=models.CharField(max_length=1000)
    gst=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return f"{self.name}"
    
class ContactEnquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    question=models.TextField()
    def __str__(self):
        return f"{self.name}"
