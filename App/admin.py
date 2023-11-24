from django.contrib import admin
from .models import userProfile,Gigs,Saved,Chat,Message,Question,Option,QuestionAnswer,InterviewQuestionAnswer,InterviewQuestion,Video
# Register your models here.
class modelView(admin.ModelAdmin):
    exclude = ('age', 'starting_rate','maximum_rate','response_time','job')

admin.site.register(userProfile,modelView)
admin.site.register(Gigs)
admin.site.register(Saved)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(InterviewQuestionAnswer)
admin.site.register(InterviewQuestion)
admin.site.register(Video)