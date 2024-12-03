# Ex02 Django ORM Web Application
## Date: 4.11.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).



ENTITY RELATIONSHIP DIAGRAM

![image](https://github.com/user-attachments/assets/8078b137-26fb-48f2-8b46-04593df44afb)




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
...
admin.py

from django.contrib import admin
from .models import Bank,BankAdmin
admin.site.register(Bank,BankAdmin)

models.py

from django.db import models
from django.contrib import admin
class Bank(models.Model):
    Customer_Name=models.CharField(max_length=100)
    Customer_ID=models.IntegerField()
    Email=models.EmailField()
    Loan_ID=models.IntegerField(primary_key=True)
    Loan_Type=models.CharField(max_length=50)
 
class BankAdmin(admin.ModelAdmin):
    list_display=('Customer_Name','Customer_ID','Email','Loan_ID','Loan_Type')

...
## OUTPUT
![alt text](<raj/Screenshot (47).png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
