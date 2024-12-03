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
