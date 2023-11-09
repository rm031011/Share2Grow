from django.db import models


# Create your models here.


class Reviews(models.Model):
	ConstituencyName=models.CharField(max_length=50)
	reviews=models.CharField(max_length=400)



class UserRegist(models.Model):
	fname=models.CharField(max_length=50)
	lname=models.CharField(max_length=50)
	username=models.TextField()
	email=models.EmailField()
	password=models.CharField(max_length=30)
	cpassword=models.CharField(max_length=30)


