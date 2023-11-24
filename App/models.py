from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='profile_pic',default='sherlock.jpg')
    location = models.CharField(max_length=5000,blank=True)
    phone = models.CharField(max_length=5000,blank=True)
    skills = models.CharField(max_length=50000,blank=True)
    age = models.IntegerField(default=18,blank=True)
    starting_rate = models.IntegerField(default=0,blank=True)
    maximum_rate = models.IntegerField(default=10,blank=True)
    job = models.CharField(max_length=50000,default="")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    qualification = models.CharField(max_length=5000,blank = True)
    response_time = models.IntegerField(default=1,blank=True)
    reg_no = models.CharField(default=0,blank=True,max_length=5000)
    company_name = models.CharField(max_length=50000,default="",blank=True)
    company_location = models.CharField(max_length=50000,blank=True)
    company_phone = models.IntegerField(default=0000000000,blank=True)
    

    is_company = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " profile"


class Gigs(models.Model):
    class Meta:
        verbose_name = "Post"
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gig_images')
    location = models.CharField(max_length=5000)
    phone = models.CharField(max_length=5000)
    title = models.CharField(max_length=50000)
    description = models.CharField(max_length=500000)
    price = models.IntegerField(default=0)
    delivery_time = models.IntegerField(default=1)
    response_time = models.IntegerField(default=1)
    category = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return self.user.username + " gig"


class Saved(models.Model):
    class Meta:
        verbose_name = "Application"
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    gig = models.ForeignKey(Gigs,on_delete=models.CASCADE)
    gig_pk = models.IntegerField(default=0)
    status = models.CharField(max_length=10000,default="",blank=True)
    
    def __str__(self):
        return self.user.username + " saved"


class Chat(models.Model):

    from_user = models.CharField(max_length=5000)
    to_user = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.from_user + " chat"


class Message(models.Model):

    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    from_user = models.CharField(max_length=5000)
    to_user = models.CharField(max_length=5000)
    message = models.CharField(max_length=50000)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "message"
    
class Question(models.Model):

    question = models.CharField(max_length=50000)
    answer = models.CharField(max_length=50000,default="")
    def __str__(self):
        return self.question 


class Option(models.Model):

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=50000)
    def __str__(self):
        return self.answer + " option" 


class QuestionAnswer(models.Model):

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    option = models.ForeignKey(Option,on_delete=models.CASCADE)
    def __str__(self):
        return self.question.question + " Answer"

class InterviewQuestion(models.Model):

    question = models.CharField(max_length=50000)
    answer = models.CharField(max_length=50000,default="")
    def __str__(self):
        return self.question 


class InterviewQuestionAnswer(models.Model):

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=50000)
    def __str__(self):
        return self.answer + " option" 
    
class Video(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.FileField(upload_to='gig_videos') 
    title = models.CharField(max_length=50000)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username + " video"