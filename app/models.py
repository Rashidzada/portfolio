from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    gender = models.CharField(max_length=100, blank=True, choices=(('male','Male'),('female','Female')),default='Male')
    address = models.CharField(max_length=233,blank=True)
    picture = models.ImageField(upload_to='profile_images/',blank=True)
    skill = models.ManyToManyField('Skill')
    education = models.ManyToManyField('Education')
    professionalexperience = models.ManyToManyField('ProfessionalExperience')

    def __str__(self):
        return f'{self.user.username}'


class Skill(models.Model):
    skill_name = models.CharField(max_length=200, blank=True,unique=True)
    hands_on = models.IntegerField(blank=True,default=0)
    
    def __str__(self):
        return self.skill_name


class Education(models.Model):
    degree_name = models.CharField(max_length=233, unique=True)
    started_at = models.DateField()
    ended_at = models.DateField()
    institute = models.CharField(max_length=233)
    grade = models.CharField(max_length=1,default='A',blank=True)
    division = models.CharField(max_length=20,blank=True,default='First',choices=(('first','First'),('second','Second'),('third',"Third")))

    def __str__(self):
        return self.degree_name
    


class ProfessionalExperience(models.Model):
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    degree_name = models.CharField(max_length=200)
    # company = models.CharField(max_length=200)
    institute = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.degree_name}'

