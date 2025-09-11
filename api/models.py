from django.db import models

class Algeria_cities(models.Model):
   num=models.IntegerField()
   commune_name= models.CharField(max_length=255)   
   commune_name_ascii=models.CharField(max_length=255)   
   daira_name=models.CharField(max_length=255) 
   daira_name_ascii=models.CharField(max_length=255) 
   wilaya_code =models.CharField(max_length=255) 
   wilaya_name =models.CharField(max_length=255) 
   wilaya_name_ascii =models.CharField(max_length=255) 

class Algeria_Wilaya(models.Model):
   wilaya_code =models.PositiveSmallIntegerField() 
   wilaya_name =models.CharField(max_length=255) 
   wilaya_name_ascii =models.CharField(max_length=255) 
   class Meta:
        ordering = ['wilaya_code'] 
   def __str__(self):
       return self.wilaya_name    