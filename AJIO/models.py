from django.db import models

# Create your models here.

class MainData(models.Model):
    Image_Src = models.CharField(max_length=255)
    Brand_Name = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Stars = models.IntegerField()
    Rating = models.CharField(max_length=255)
    Actual_Price = models.IntegerField()
    Price = models.IntegerField()
    Discount = models.IntegerField()
    Value = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.Name
    
class MensData(MainData):
    pass

class WomensData(MainData):
    pass

class KidsData(MainData):
    pass

class LoginData(models.Model):
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=25)
    Security = models.CharField(max_length=255)
    
class OrdersData(MainData):
    Username = models.CharField(max_length=25)
    Order_Id = models.CharField(max_length=255)
   
    def __str__(self):
        return f"{self.Username} - {self.Name}"