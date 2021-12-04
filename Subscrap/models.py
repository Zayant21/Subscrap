from django.forms import ModelForm, Textarea
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import Func, F, Sum
from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class students(AbstractBaseUser):
	email= models.EmailField(max_length=254,unique=True)
	username= models.CharField(max_length=30,unique=True)
	firstname = models.CharField(max_length=30, blank = True)
	lastname = models.CharField(max_length=30, blank = True)
	profilepic = models.ImageField(upload_to='images', default= 'images/defaultuser.png')
	Bio = models.TextField( blank = True)
	#------------------------------------------------------------------------------------#
	date_joined= models.DateTimeField(verbose_name='date joined',auto_now_add=True)
	last_login= models.DateTimeField(verbose_name='last login',auto_now=True)
	is_admin= models.BooleanField(default=False)
	is_active= models.BooleanField(default=True)
	is_staff= models.BooleanField(default=False)
	is_superuser= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

	class Meta:
		db_table = "students"



class sublist(models.Model):
	Monthly = 1
	Trimester = 3
	Yearly = 12
	RENEWALCYCLE_CHOICES =(
		(Monthly,"Monthly"),
		(Trimester,"Trimester"),
		(Yearly,"Yearly"),
	) 

	Music = 'Music'
	Video = 'Video'
	News = 'News'
	Lifestyle = 'Lifestyle'
	Access = 'Online Access'
	
	SUBTYPE_CHOICES =(
	(Music , "Music"),
	(Video , "Video"),
	(News , "News"),
	(Lifestyle , "Lifestyle"),
	(Access , "Online Access"),
	) 
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	name = models.CharField(max_length=150)
	cost = models.FloatField(default = 0)
	renewalcycle = models.IntegerField(choices= RENEWALCYCLE_CHOICES, default = Monthly)
	subtype = models.CharField(max_length= 50, choices = SUBTYPE_CHOICES,blank = True)
	image = models.ImageField(upload_to='images', default= 'images/logoemblem.png')
	website = models.URLField(max_length=250, default = 'http://127.0.0.1:8000/main/')
	#-------------------------------------------------#
	startDate = models.DateField(default=datetime.datetime.now())
	dueDate = models.DateField(null=True, blank=True)
	is_active = models.BooleanField(default=True)
	is_autorenewal = models.BooleanField(default=True)
	is_notified = models.BooleanField(default=False)
	Notes = models.TextField( blank = True)

	
	def __str__(self):
		return self.name

	
	class Meta:
		db_table = "sublist"


class prebuildsublist(models.Model):

	Music = 'Music'	
	Video = 'Video'
	News = 'News'
	Lifestyle = 'Lifestyle'
	Access = 'Access'

	SUBTYPE_CHOICES =(
	(Music , "Music"),
	(Video , "Video"),
	(News , "News"),
	(Lifestyle , "Lifestyle"),
	(Access , "Online Access"),
	) 

	name = models.CharField(max_length=150)
	image = models.ImageField(upload_to='images/prestored')
	website = models.URLField(max_length=250, blank = True)
	subtype = models.CharField(max_length= 50, choices = SUBTYPE_CHOICES, blank = True)

	def __str__(self):
		return self.name
	
	class Meta:
		db_table = "prebuildsublist"

	
class Payment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    month = models.CharField(max_length=15, blank = True)
    total = models.FloatField()

class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()