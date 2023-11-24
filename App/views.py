from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from .models import userProfile,Gigs,Saved,Chat,Message,Question,Option,QuestionAnswer,InterviewQuestion,InterviewQuestionAnswer,Video
# Create your views here.

def homepage(request):
    request.session['login_error'] = 0
    if request.user.is_authenticated:
        
        profile = userProfile.objects.filter(user = request.user).first()
        gigs = Gigs.objects.all().order_by('-date')
        gigs_list = []
        for gig in gigs:
            save = Saved.objects.filter(Q(gig_pk = gig.pk) & Q(user = request.user)).first()
            if save:
                saved = 1
            else:
                saved = 0
            user = User.objects.filter(pk = gig.user.pk).first()
            p = userProfile.objects.filter(user = user).first()
            print("save;",saved )
            dictionary = {'title':gig.title,"user":gig.user,"image":gig.image.url,"price":gig.price,"pk":gig.pk,"avatar":p.image.url,"saved":saved,"date":gig.date} 
            gigs_list.append(dictionary)
    else:
        profile = ''
        gigs = Gigs.objects.all()
        gigs_list = []
        for gig in gigs:
            try:
                save = Saved.objects.filter(Q(gig_pk = gig.pk) & Q(user = request.user)).first()
                if save:
                    saved = 1
                else:
                    saved = 0
            except:
                saved = 0
            user = User.objects.filter(pk = gig.user.pk).first()
            p = userProfile.objects.filter(user = user).first()
            dictionary = {'title':gig.title,"user":gig.user,"image":gig.image.url,"price":gig.price,"pk":gig.pk,"avatar":p.image.url,"saved":saved,"date":gig.date} 
            gigs_list.append(dictionary)

    # all_from_chats = Chat.objects.filter(from_user = request.user.username)
    # final_from_chats = []
    # print(all_from_chats)
    # for chat in all_from_chats:
    #     # if chat.from_user != request.user.username 
        
    #     cht = Chat.objects.filter(from_user = request.user.username).first()
    #     u = User.objects.filter(username = cht.to_user).first()
    #     pro = userProfile.objects.filter(user = u).first()
    #     message = Message.objects.filter(Q(from_user = request.user.username) & Q(to_user = chat.to_user)).all().order_by('-date').first()
    #     print('from ===',message.message)
    #     ch = {"username":chat.to_user,"image":pro.image.url,"message":message.message}
    #     final_from_chats.append(ch)
    #     # print(ch)
    

    # all_to_chats = Chat.objects.filter(to_user = request.user.username)
    # final_to_chats = []
    # print("====",all_to_chats)
    # for chat in all_to_chats:
        
        
    #     cht = Chat.objects.filter(to_user = request.user.username).first()
    #     u = User.objects.filter(username = cht.from_user).first()
    #     pro = userProfile.objects.filter(user = u).first()
    #     # message = Message.objects.filter(to_user = request.user.username).last()
    #     message = Message.objects.filter(Q(from_user = cht.to_user) & Q(to_user = chat.from_user)).all().order_by('-date').first()

    #     ch = {"username":chat.from_user,"image":pro.image.url,"message":message.message}
    #     final_from_chats.append(ch)
    #     print(ch)
    #     print('to ===',message.message)
    all_chats_to = []
    chats = Chat.objects.filter(to_user = request.user)
    for chat in chats:
        all_chats_to.append({"username":chat.from_user,"image":"pro.image.url","message":"mesg.message"})
    
    chats2 = Chat.objects.filter(from_user = request.user)
    for chat in chats2:
        all_chats_to.append({"username":chat.to_user,"image":"pro.image.url","message":"mesg.message"})

    profiles = userProfile.objects.filter(is_company = False).order_by('-date')
    profiles_list = []

    for p in profiles:
        if p.user.username != "guestuser":
            prof = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job,"is_company":p.is_company,"age":p.age}
            profiles_list.append(prof)

    return render(request,'index.html',context = {'profile':profile,"gigs":gigs_list[0:4],'chats':all_chats_to,"profiles":profiles_list[:4]})


message = 0
reg_error = 0


def homepage1(request):
    return HttpResponseRedirect(reverse('homepage'))

def register(request):
    print("************",request.POST.get('username'))
    if request.method == 'POST':
        user = User.objects.create(username = request.POST.get('username'),first_name=request.POST.get('firstname'),last_name=request.POST.get('lastname'),email=request.POST.get('email'))
        user.set_password(request.POST.get('password'))
        user.save()

        user = User.objects.filter(username=request.POST.get('username')).first()
        
        profile = userProfile.objects.create(user=user,phone  = request.POST.get('phone'),age = request.POST.get('age'), image = request.FILES['image'],skills = request.POST.get('skills'),location = request.POST.get('country'),is_company = False,qualification = request.POST.get('qualification'),reg_no = request.POST.get('admno'))
        profile.save()
        

    return HttpResponseRedirect(reverse('homepage'))


def registerNormal(request):
    print("************",request.POST.get('username'))
    if request.method == 'POST':
        user = User.objects.create(username = request.POST.get('username'),first_name=request.POST.get('firstname'),last_name=request.POST.get('lastname'),email=request.POST.get('email'))
        user.set_password(request.POST.get('password'))
        user.save()

        user = User.objects.filter(username=request.POST.get('username')).first()
        
        profile = userProfile.objects.create(user=user,phone  = request.POST.get('phone'),age = request.POST.get('age'), image = request.FILES['image'],skills = request.POST.get('skills'),location = request.POST.get('country'),job = request.POST.get('job'),is_freelancer = False)
        profile.save()
        

    return HttpResponseRedirect(reverse('homepage'))


def companyRegister(request):
    print("************",request.POST.get('username'))
    if request.method == 'POST':
        user = User.objects.create(username = request.POST.get('username'),first_name=request.POST.get('firstname'),email=request.POST.get('email'))
        user.set_password(request.POST.get('password'))
        user.save()

        user = User.objects.filter(username=request.POST.get('username')).first()
        
        profile = userProfile.objects.create(user=user,phone  = request.POST.get('phone'), image = request.FILES['image'],location = request.POST.get('country'),is_company = True,company_location = request.POST.get('lastname'),company_name = request.POST.get('firstname'))
        profile.save()
        

    return HttpResponseRedirect(reverse('homepage'))

def checkLogin(request):
    email = request.POST.get('email')
    print(email)
    
    try:
        username = User.objects.get(email=email.lower()).username
    except:
        username = ""

    password = request.POST.get('password')

    user = authenticate(username = username,password = password)
    if user:
        print(username)
        return JsonResponse({"message":0})
            
    else:
        print("No user found")
        return JsonResponse({"message":1})
        

def checkSignup(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    
    u = User.objects.filter(username = username).first()
    
    if u == None:
        message = 0
    else:
        message = 1
    
    return JsonResponse({"message":message})


def checkUsername(request):

    user = User.objects.filter(username = request.POST.get('username')).first()
    if user == None:
        exists = 0
    else:
        exists = 1

    return JsonResponse({"result":exists})

login_error = 0

def user_login(request):
    request.session['login_error'] = 0
    if request.method == 'POST':
        email = request.POST.get('email')
        print("-=-=-=-",request.POST.get('email'))
        password = request.POST.get('password')
        try:
            username = User.objects.get(email=email.lower()).username
            user = authenticate(username = username ,password = password)
            if user:

                if user.is_active:
                    login(request, user)
                    print("successful login")
                    request.session['login_error'] = 0
                    return HttpResponseRedirect(reverse('homepage'))
            else:
                request.session['login_error'] = 1
                return HttpResponseRedirect(reverse('showLogin'))
        except:
            request.session['login_error'] = 1
            return HttpResponseRedirect(reverse('showLogin'))



    
    
@login_required
def user_logout(request):

    logout(request)


    return HttpResponseRedirect(reverse('homepage'))


def post(request):
    
    gig = Gigs.objects.create(user = request.user,image = request.FILES['image'],title = request.POST.get('title'),description = request.POST.get('description'),price = request.POST.get('price'),location = request.POST.get('country'),category = request.POST.get('category'),response_time = request.POST.get('response'),delivery_time = request.POST.get('delivery'))
    return HttpResponseRedirect(reverse('homepage'))


def save(request):
    
    gig = Gigs.objects.filter(pk = request.POST.get('pk')).first()
    save = Saved.objects.filter(Q(user = request.user) & Q(gig_pk = request.POST.get('pk')))
    if save:
        save = Saved.objects.filter(Q(user = request.user) & Q(gig_pk = request.POST.get('pk')))
        save.delete()
    else:
        saved = Saved.objects.create(gig = gig,gig_pk = request.POST.get('pk'),user = request.user)

    print(save)
    return JsonResponse({"result":0})


def gigView(request,pk):
    gig = Gigs.objects.filter(pk = pk).first()
    profile = userProfile.objects.filter(user = gig.user).first()
    try:
        log_user = userProfile.objects.filter(user = request.user).first()
    except:
        g_user = User.objects.filter(username = "guestuser").first()
        log_user = userProfile.objects.filter(user = g_user).first()
    gigs = Gigs.objects.filter(pk = pk).first()
    gigs_list = []
    
    chat = Chat.objects.filter(Q(from_user = request.user.username) & Q(to_user = gig.user.username)).first()
    messages = Message.objects.filter(chat = chat).all()
    if not request.user.is_authenticated:
        save = Saved.objects.filter(Q(gig_pk = gig.pk) & Q(user = g_user)).first()
    else:
        save = Saved.objects.filter(Q(gig_pk = gig.pk) & Q(user = request.user)).first()
    if save:
        saved = 1
    else:
        saved = 0
    user = User.objects.filter(pk = gig.user.pk).first()
    p = userProfile.objects.filter(user = user).first()
    print("save;",saved )
    dictionary = {'title':gig.title,"user":gig.user,"image":gig.image.url,"price":gig.price,"pk":gig.pk,"avatar":p.image.url,"saved":saved,"date":gig.date,"delivery_time":gig.delivery_time,"response_time":gig.response_time,"description":gig.description,"category":gig.category,"date":gig.date,"location":gig.location} 
    gigs_list.append(dictionary)

    profile_user = userProfile.objects.filter(user = gig.user).first()
    profile_list = []
    print(profile_user)
    
    prof = {"username":profile_user.user.username,"location":profile_user.location,"starting":profile_user.starting_rate,"ending":profile_user.maximum_rate,"skills":profile_user.skills.split(',')[:2],"image":profile_user.image.url,"pk":profile_user.user.pk,"company":profile_user.is_company}
    profile_list.append(prof)


    profiles_list2 = []

    profiles = userProfile.objects.filter(is_company = False).order_by('-date')

    users = []
    posts = Saved.objects.filter(gig= gig)
    for us in posts:
        # print("status : ",us.status)
        # if us.status == "":
        #     users.append(us.user)
        users.append(us.user)
    print("[+] Users : ",users)
    prfs = []

    for u in users:
        pf = userProfile.objects.filter(user = u).first()
        prfs.append(pf)
    
    print("[+] Profiles : ",prfs)

    for p in prfs:
        if p.user.username != "guestuser":
            ps = Saved.objects.filter(Q(gig= gig) & Q(user = p.user)).first()
            if ps.status == "":
                prof2 = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job,"age":p.age,"is_company":p.is_company,"status":False,"text":ps.status}
            else:
                prof2 = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job,"age":p.age,"is_company":p.is_company,"status":True,"text":ps.status}

            profiles_list2.append(prof2)
    
    print("List [=] : ",profiles_list2)
    return render(request,'gigView.html',{'profile':profile,"gig":dictionary,"saved":saved,"logged_user":log_user,"messages":messages,"gig_profile":prof,"profiles":profiles_list2[:4],"log_profile":log_user})


def saved(request):
    profile = userProfile.objects.filter(user = request.user).first()
    saved = Saved.objects.filter(user = request.user)
    gigs_list = []
    for gig in saved:
        save = Saved.objects.filter(Q(gig_pk = gig.gig.pk) & Q(user = request.user)).first()
        if save:
            saved = 1
        else:
            saved = 0
        user = User.objects.filter(pk = gig.user.pk).first()
        p = userProfile.objects.filter(user = user).first()
        print("save;",saved )
        dictionary = {'title':gig.gig.title,"user":gig.gig.user,"image":gig.gig.image.url,"price":gig.gig.price,"pk":gig.gig.pk,"avatar":p.image.url,"saved":saved,"date":gig.gig.date,"status":save.status} 
        gigs_list.append(dictionary)
        
    profiles = userProfile.objects.filter(is_company = False).order_by('-date')

    profiles_list = []

    for p in profiles:
        if p.user.username != "guestuser":
            prof = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job,"age":p.age,"is_company":p.is_company}
            profiles_list.append(prof)

    return render(request,'saved.html',{'profile':profile,"gigs":gigs_list,"profiles":profiles_list[:4]})


def gigs(request):
    if request.user.is_authenticated:
        profile = userProfile.objects.filter(user = request.user).first()
    else:
        profile = userProfile.objects.filter(user = User.objects.filter(username = "guestUser").first()).first()
    try:
        saved = Saved.objects.filter(user = request.user)
    except:
        saved =[]
    gigs = Gigs.objects.all().order_by('-date')
    gigs_list = []
    for gig in gigs:
        try:
            save = Saved.objects.filter(Q(gig_pk = gig.pk) & Q(user = request.user)).first()
        except:
            save = None

        if save:
            saved = 1
        else:
            saved = 0
        user = User.objects.filter(pk = gig.user.pk).first()
        p = userProfile.objects.filter(user = user).first()
            # print("save;",saved )
        dictionary = {'title':gig.title,"user":gig.user,"image":gig.image.url,"price":gig.price,"pk":gig.pk,"avatar":p.image.url,"saved":saved,"date":gig.date} 
        gigs_list.append(dictionary)

    profiles = userProfile.objects.filter(is_company = False).order_by('-date')

    profiles_list = []

    for p in profiles:
        if p.user.username != "guestuser":
            prof = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job,"age":p.age,"is_company":p.is_company}
            profiles_list.append(prof)

    return render(request,'gigs.html',{'profile':profile,"gigs":gigs_list,"profiles":profiles_list[:4]})


def sendMsg(request):

    chat = Chat.objects.filter(Q(from_user = request.POST.get('from_user')) & Q(to_user = request.POST.get('to_user'))).first()

    if chat:
        # chatObj = Chat.objects.create(from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))
        message = Message.objects.create(chat = chat,message = request.POST.get("message"),from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))
    else:
        chatObj = Chat.objects.create(from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))
        message = Message.objects.create(chat = chatObj,message = request.POST.get("message"),from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))

   
    return JsonResponse({"result":0})


def sendMsg1(request):

    chat = Chat.objects.filter(Q(from_user = request.POST.get('from_user')) & Q(to_user = request.POST.get('to_user'))).first()

    if chat:
        # chatObj = Chat.objects.create(from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))
        message = Message.objects.create(chat = chat,message = request.POST.get("message"),from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))
    else:
        chat = Chat.objects.filter(Q(from_user = request.POST.get('to_user')) & Q(to_user = request.POST.get('from_user'))).first()
        message = Message.objects.create(chat = chat,message = request.POST.get("message"),from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))

   
    return JsonResponse({"result":0})

def showMessages(request):

    
    chat = Chat.objects.filter(Q(from_user = request.POST.get('from_user')) & Q(to_user = request.POST.get("to_user"))).first()
    
    if chat:
        chat = Chat.objects.filter(Q(from_user = request.POST.get('from_user')) & Q(to_user = request.POST.get("to_user"))).first()

    else:
        chat = Chat.objects.filter(Q(from_user = request.POST.get('to_user')) & Q(to_user = request.POST.get("from_user"))).first()

    user = User.objects.filter(username = request.POST.get('to_user')).first()
    profile = userProfile.objects.filter(user = user).first()
    print(profile)
    messages = Message.objects.filter(chat = chat).all()

    msg_list = []
    for message in messages:
        m = {"from_user":message.from_user,"to_user":message.to_user,"message":message.message}

        msg_list.append(m)


    return JsonResponse({"message":msg_list,"image":profile.image.url,"avg":profile.location})



def delete(request,pk):
    
    gig = Gigs.objects.filter(pk = pk).first()
    gig.delete()

    return HttpResponseRedirect(reverse('homepage'))


def profileView(request,pk):
    try:
        profile2 = userProfile.objects.filter(user = request.user).first()
    except:
        u = User.objects.filter(username = "guestuser").first()
        profile2 = userProfile.objects.filter(user = u).first()
    user = User.objects.filter(pk = pk).first()
    profile = userProfile.objects.filter(user = user).first()
    gigs = Gigs.objects.filter(user = user)
    gigs_list = []
    chat = Chat.objects.filter(Q(from_user = request.user.username) & Q(to_user = user.username)).first()
    messages = Message.objects.filter(chat = chat).all()
    for gig in gigs:
        try:
            save = Saved.objects.filter(Q(gig_pk = gig.pk) & Q(user = request.user)).first()
            if save:
                saved = 1
            else:
                saved = 0
        except:
            saved = 0
        user = User.objects.filter(pk = pk).first()
        p = userProfile.objects.filter(user = user).first()
        dictionary = {'title':gig.title,"user":gig.user,"image":gig.image.url,"price":gig.price,"pk":gig.pk,"avatar":p.image.url,"saved":saved,"date":gig.date} 
        gigs_list.append(dictionary)

    profiles = userProfile.objects.filter(is_company = False).order_by('-date')

    profiles_list = []

    for p in profiles:
        if p.user.username != "guestuser":
            prof = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job}
            profiles_list.append(prof)
    videos = Video.objects.filter(user =user)
    return render(request,'profileView.html',{"gigs":gigs_list,"userProfile":profile,"messages":messages,"skills":profile.skills.split(',')[:3],"profile":profile2,"profiles":profiles_list[:4],"videos":videos})



def search(request):
    profile2 = userProfile.objects.filter(user = request.user).first()
    
    gigs = Gigs.objects.filter(Q(location__icontains=request.POST.get('country')) & Q(category__icontains=request.POST.get('category')) | Q(title__icontains = request.POST.get('title')))
    gigs_list = []
    
    for gig in gigs:
        try:
            save = Saved.objects.filter(Q(gig_pk = gig.pk) & Q(user = request.user)).first()
            if save:
                saved = 1
            else:
                saved = 0
        except:
            saved = 0
        user = User.objects.filter(username = gig.user.username).first()
        p = userProfile.objects.filter(user = user).first()
        dictionary = {'title':gig.title,"user":gig.user,"image":gig.image.url,"price":gig.price,"pk":gig.pk,"avatar":p.image.url,"saved":saved,"date":gig.date} 
        gigs_list.append(dictionary)
    
    profiles = userProfile.objects.filter(is_company = False).order_by('-date')

    profiles_list = []

    for p in profiles:
        if p.user.username != "guestuser":
            prof = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job}
            profiles_list.append(prof)

    return render(request,'search.html',{"gigs":gigs_list,"profile":profile2,"profiles":profiles_list[:4]})


def editAccount(request):
    if request.method == 'POST':
        if(request.POST.get('password') == ""):
            user = User.objects.filter(username = request.user.username).first()
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.email = request.POST.get('email')
            # user.set_password(request.POST.get('password'))
            user.save()
            if str(request.FILES.get('profilePic')) == None:
                profile = userProfile.objects.filter(user=user).first()
                profile.phone = request.POST.get('phone')
                profile.age = request.POST.get('age')
                profile.skills = request.POST.get('skills')
                profile.location = request.POST.get('country')
                profile.job = request.POST.get('job')
                profile.save()
            else:
                profile = userProfile.objects.filter(user=user).first()
                profile.phone = request.POST.get('phone')
                profile.age = request.POST.get('age')
                profile.skills = request.POST.get('skills')
                profile.location = request.POST.get('country')
                profile.image = request.FILES.get('profilePic')
                profile.job = request.POST.get('job')
                profile.save()
        
        else:
            user = User.objects.filter(username = request.user.username).first()
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password'))
            user.save()
            if str(request.FILES.get('profilePic')) == None:
                profile = userProfile.objects.filter(user=user).first()
                profile.phone = request.POST.get('phone')
                profile.age = request.POST.get('age')
                profile.skills = request.POST.get('skills')
                profile.location = request.POST.get('country')
                profile.response_time = request.POST.get('response')
                profile.job = request.POST.get('job')
                profile.save()
            else:
                profile = userProfile.objects.filter(user=user).first()
                profile.phone = request.POST.get('phone')
                profile.age = request.POST.get('age')
                profile.skills = request.POST.get('skills')
                profile.location = request.POST.get('country')
                profile.image = request.FILES.get('profilePic')
                profile.response_time = request.POST.get('response')
                profile.job = request.POST.get('job')
                profile.save()

       

    return HttpResponseRedirect(reverse('homepage'))



def deleteUser(request,pk):

    user = User.objects.filter(pk = pk).first()
    user.delete()

    return HttpResponseRedirect(reverse('homepage'))


def editPost(request,pk):
    print("image ====",request.FILES.get('image'))
    if request.FILES.get('image') == None:
        gig = Gigs.objects.filter(pk = pk).first()
        print(gig)
        gig.title = request.POST.get('title')
        gig.description = request.POST.get('description')
        gig.location = request.POST.get('country')
        gig.price = request.POST.get('price')
        gig.category = request.POST.get('category')
        gig.response_time = request.POST.get('response')
        gig.delivery_time = request.POST.get('delivery')
        gig.save()
    else:
        gig = Gigs.objects.filter(pk = pk).first()
        gig.title = request.POST.get('title')
        gig.description = request.POST.get('description')
        gig.location = request.POST.get('country')
        gig.price = request.POST.get('price')
        gig.category = request.POST.get('category')
        gig.response_time = request.POST.get('response')
        gig.delivery_time = request.POST.get('delivery')
        gig.image = request.FILES['image']
        gig.save()

    return HttpResponseRedirect(reverse('homepage'))



def freelancers(request):
    profiles = userProfile.objects.filter(is_company = False).order_by('-date')

    profiles_list = []

    for p in profiles:
        if p.user.username != "guestuser":
            prof = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job,"age":p.age,"is_company":p.is_company}
            profiles_list.append(prof)
    if request.user.is_authenticated:
        profile = userProfile.objects.filter(user = request.user).first()
    else:
        profile = userProfile.objects.filter(user = User.objects.filter(username = "guestUser").first()).first()
    return render(request,'freelancers.html', {"profiles":profiles_list,"profile":profile})


def showLogin(request):
    return render(request,'login.html')

def showSignupNormal(request):
    return render(request,'signup.html')

def createPost(request):
    profile = userProfile.objects.filter(user = request.user).first()
    return render(request,'createPost.html',{"profile":profile})

def editGig(request,pk):
    gig = Gigs.objects.filter(pk = pk).first()
    profile = userProfile.objects.filter(user = request.user).first()
    return render(request,'editGig.html',{"profile":profile,"gig":gig})

def error(request):
    request.session['login_error'] = 0
    return JsonResponse({"message":"1"})



def convert_pdf_to_txt(path):
    
    resource_manager = PDFResourceManager()
    file_handle = io.StringIO()
    converter = TextConverter(resource_manager, file_handle, codec='utf-8', laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
    text = file_handle.getvalue()
    # close open handles
    converter.close()
    file_handle.close()
    return text

import spacy
from spacy.matcher import PhraseMatcher
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io

from django.core.files.storage import FileSystemStorage
import pickle
def upload(request):
    
# Define a function to convert pdf to text
    file = request.FILES.get('file')
    fss = FileSystemStorage()
    filename = fss.save(file.name,file)
    url = fss.url(filename)

# Load the spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Open the pdf file and read its text
    resume_text = convert_pdf_to_txt("media/"+filename)
    import os
    import openai

    openai.api_key = "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"

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="identify the skills from this, give the skills sperated by comma: " + resume_text,
    temperature=0.7,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    # Convert the text to lowercase
    resume_text = resume_text.lower()
    print(response)
    # Define the list of skills
    skills = "python, javascript, flask, django, sql, mysql, postgresql, agile, ai, flutter, html, css ,js,javascript,machine learning,deep learning,artificial intelligence"

    # Convert the skills string into a list
    skills_list = skills.split(", ")

    # Create the PhraseMatcher object and add the skill phrases to be matched
    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp(skill) for skill in skills_list]
    matcher.add("SKILLS", None, *patterns)

    # Process the text with spaCy
    doc = nlp(resume_text)

    # Call the matcher on the doc
    matches = matcher(doc)

    # Extract the matched skills
    matched_skills = [doc[start:end] for match_id, start, end in matches]

    # Print the matched skills
    print("Matched skills:", [skill.text for skill in matched_skills])
    loaded_model = pickle.load(open("naive_job.sav", 'rb'))

    print(str(response["choices"][0].text).replace("\n\n","").replace("Skills:", ""))
    result = loaded_model.predict([str(response["choices"][0].text).replace("\n\n","").replace("Skills:", "")])
    print(result)
    
    profile = userProfile.objects.filter(user = request.user).first()
    saved = Saved.objects.filter(user = request.user)
    gigs_list = []
    gigs_all = Gigs.objects.filter(category = result[0])
    for gig in gigs_all:
        save = Saved.objects.filter(Q(gig_pk = gig.pk) & Q(user = request.user)).first()
        if save:
            saved = 1
        else:
            saved = 0
        user = User.objects.filter(pk = gig.user.pk).first()
        p = userProfile.objects.filter(user = user).first()
        print("save;",saved )
        dictionary = {'title':gig.title,"user":gig.user,"image":gig.image.url,"price":gig.price,"pk":gig.pk,"avatar":p.image.url,"saved":saved,"date":gig.date} 
        gigs_list.append(dictionary)

    profiles = userProfile.objects.filter(is_company = False).order_by('-date')

    profiles_list = []

    for p in profiles:
        if p.user.username != "guestuser":
            prof = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job,"age":p.age,"is_company":p.is_company}
            profiles_list.append(prof)

    return render(request,'recommendation.html',{'profile':profile,"gigs":gigs_list,"profiles":profiles_list[:4]})

    # return JsonResponse({"result":result[0]})


def mocktest(request):
    questions_list = []
    questions = Question.objects.all()
    for question in questions:
        options = Option.objects.filter(question = question)
        questions_list.append({"question":question,"options":options})
    print(questions_list)
    profile2 = userProfile.objects.filter(user = request.user).first()
    return render(request,'mocktest.html',{"profile":profile2,"questions":questions_list})


def getResult(request):
    

    questions_answer = []
    questions = Question.objects.all()
    for question in questions:
        # options = Option.objects.filter(question = question)
        questions_answer.append(question.answer)
    # print(questions_number)
    question_count = Question.objects.all().count()
    
    question_number = []
    for question in questions:
        # options = Option.objects.filter(question = question)
        question_number.append(question.pk)
    
    all_answers = []

    for q in questions:
        all_answers.append(q.answer)
    print("Answers ",all_answers)
    
    answers = []
    for i in range(0,len(question_number)):
        answers.append(request.POST.get('question'+str(question_number[i])))
    print("User answers : ",answers)

    # list1 = ['9966', 'eddy current loss']
    # list2 = ['9980', 'eddy current loss']

    list1 = all_answers
    list2 = answers

    num_correct = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            num_correct += 1

    mark = str(num_correct) + " / " + str(len(list1))
    print("Marks = ",mark)
    profile2 = userProfile.objects.filter(user = request.user).first()
    questions_list = []

    questions = Question.objects.all()
    i = 0
    for question in questions:
        options = ["test"]
        questions_list.append({"question":question,"options":options,"answer":answers[i]})
        i = i + 1
    print(questions_list)

    return render(request,'result.html',{"profile":profile2,"questions":questions_list,"score":mark})


def companySignup(request):
    return render(request,'normalSignup.html')

def interview(request):
    questions_list = []
    questions = InterviewQuestion.objects.all()
    # for question in questions:
    #     options = InterviewQuestionAnswer.objects.filter(question = question)
    #     questions_list.append({"question":question,"options":options})
    # print(questions_list)
    profile2 = userProfile.objects.filter(user = request.user).first()
    return render(request,'interview.html',{"profile":profile2,"questions":questions})

def resume(request):
    try:
        profile2 = userProfile.objects.filter(user = request.user).first()
    except:
        u = User.objects.filter(username = "guestuser").first()
        profile2 = userProfile.objects.filter(user = u).first()
    user = User.objects.filter(pk = request.user.pk).first()
    profile = userProfile.objects.filter(user = user).first()
    gigs = Gigs.objects.filter(user = user)
    gigs_list = []
    
    for gig in gigs:
        try:
            save = Saved.objects.filter(Q(gig_pk = gig.pk) & Q(user = request.user)).first()
            if save:
                saved = 1
            else:
                saved = 0
        except:
            saved = 0
        user = User.objects.filter(pk = request.user.pk).first()
        p = userProfile.objects.filter(user = user).first()
        dictionary = {'title':gig.title,"user":gig.user,"image":gig.image.url,"price":gig.price,"pk":gig.pk,"avatar":p.image.url,"saved":saved,"date":gig.date} 
        gigs_list.append(dictionary)

    profiles = userProfile.objects.filter(is_company = False).order_by('-date')

    profiles_list = []

    for p in profiles:
        if p.user.username != "guestuser":
            prof = {"username":p.user.username,"location":p.location,"starting":p.starting_rate,"ending":p.maximum_rate,"skills":p.skills.split(',')[:2],"image":p.image.url,"pk":p.user.pk,"job":p.job}
            profiles_list.append(prof)
   
    return render(request,'resume.html',{"gigs":gigs_list,"userProfile":profile,"skills":profile.skills.split(',')[:3],"profile":profile2,"profiles":profiles_list[:4],"name":request.POST.get('firstname') + " "+ request.POST.get('lastname'),"gender":request.POST.get('gender'),"email":request.POST.get('email'),"phone":request.POST.get('phone'),"address":request.POST.get('address'),"degree":request.POST.get('degree'),"year":request.POST.get('year'),"skills_all":request.POST.get('skills'),"country":request.POST.get('country'),"image":userProfile.objects.filter(user = request.user).first().image.url,"bio":request.POST.get('bio')})


def uploadVideo(request):

    Video.objects.create(title = request.POST.get('title'),video = request.FILES['video'],user = request.user)

    return HttpResponseRedirect(reverse('homepage'))


def application(request):

    app = Saved.objects.filter(gig = Gigs.objects.filter(pk = request.POST.get('gigpk')).first(), user = User.objects.filter(pk = request.POST.get('userpk')).first()).first()
    app.status = request.POST.get('status')
    app.save()
    return gigView(request,request.POST.get('gigpk'))