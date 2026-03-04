from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail

from .models import contact_tbl,contact_map_tbl,topbar_tbl,quote_tbl,index_tbl,quote_img_tbl,testi_tbl,team_tbl,project_tbl,service_tbl,feature_sub_tbl,feature_tbl,about_tbl,about_sub_tbl,about_card_tbl

# Create your views here.

def homepageview(request):
    top_data=topbar_tbl.objects.first()
    about_data=about_tbl.objects.first()
    about_sub_data=about_sub_tbl.objects.all()
    about_card_data=about_card_tbl.objects.all()
    service_data=service_tbl.objects.all()
    feature_sub_data=feature_sub_tbl.objects.all()
    feature_data=feature_tbl.objects.first()
    project_data=project_tbl.objects.all()
    quote_data=quote_img_tbl.objects.first()
    team_data=team_tbl.objects.all()
    home_data=index_tbl.objects.all()
    
    if request.method=="GET":
       return render(request,'index.html',{'about_data':about_data,'about_sub_data':about_sub_data,'about_card_data':about_card_data,'service_data':service_data,'feature_data':feature_data,'feature_sub_data':feature_sub_data,'project_data':project_data,'quote_data':quote_data,'team_data':team_data,'home_data':home_data,'top_data':top_data})
    
          
    else:
          quote_tbl(
               q_name=request.POST.get('q_name'),
               q_email=request.POST.get('q_email'),
               q_mo_no=request.POST.get('q_mo_no'),
               q_select_ser=request.POST.get('q_select_ser'),
               q_note=request.POST.get('q_note')
          ).save()

    return redirect('index')

    

def aboutpageview(request):
    top_data=topbar_tbl.objects.first()
    about_data=about_tbl.objects.first()
    about_sub_data=about_sub_tbl.objects.all()
    about_card_data=about_card_tbl.objects.all()
    team_data=team_tbl.objects.all()
    return render(request,'about.html',{'team_data':team_data,'about_data':about_data,'about_sub_data':about_sub_data,'about_card_data':about_card_data,'top_data':top_data})


def featurepageview(request):
    top_data=topbar_tbl.objects.first()
    feature_sub_data=feature_sub_tbl.objects.all()
    feature_data=feature_tbl.objects.first()
    return render(request,'feature.html',{'feature_data':feature_data,'feature_sub_data':feature_sub_data,'top_data':top_data})





def contactpageview(request):


    contact_data=contact_map_tbl.objects.first()
 
    if request.method == "POST":

        name = request.POST.get('u_name')
        email = request.POST.get('u_email')
        subject = request.POST.get('u_subject')
        msg = request.POST.get('u_message')

        contact_tbl.objects.create(
            u_name=name,
            u_email=email,
            u_subject=subject,
            u_message=msg
        ).save

      
        
        return redirect("contact")

    return render(request, "contact.html")

    
    


from django.contrib import messages
from .models import NewsletterSubscriber

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
           
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, "You have successfully subscribed!")
            else:
                messages.info(request, "You are already subscribed.")
        else:
            messages.error(request, "Please enter a valid email.")
        return redirect('index') 
    return redirect('index')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')




























# def contactpageview(request):
#      top_data=topbar_tbl.objects.first()
#      contact_data=contact_map_tbl.objects.first()
#      if request.method=="GET":
#            return render(request,'contact.html',{'contact_data':contact_data,'top_data':top_data})
#      else:
#           contact_tbl(
#                u_name=request.POST.get('u_name'),
#                u_email=request.POST.get('u_email'),
#                u_subject=request.POST.get('u_subject'),
#                u_message=request.POST.get('u_message')



               
#           ).save()

#      return redirect('contact')    # URL name वापरा

    # return render(request,'contact.html')


def quotepageview(request):
    top_data=topbar_tbl.objects.first()
    quote_data=quote_img_tbl.objects.first()
    if request.method=="GET":
           return render(request,'quote.html',{'quote_data':quote_data,'top_data':top_data})
    else:
          quote_tbl(
               q_name=request.POST.get('q_name'),
               q_email=request.POST.get('q_email'),
               q_mo_no=request.POST.get('q_mo_no'),
               q_select_ser=request.POST.get('q_select_ser'),
               q_note=request.POST.get('q_note')
          ).save()

    return redirect('quote')      # URL name वापरा

    
    return render(request,'quote.html')


def servicepageview(request):
    top_data=topbar_tbl.objects.first()
    service_data=service_tbl.objects.all()
    return render(request,'service.html',{'service_data':service_data,'top_data':top_data})


def teampageview(request):
    top_data=topbar_tbl.objects.first()
    team_data=team_tbl.objects.all()
    return render(request,'team.html',{'team_data':team_data,'top_data':top_data})

def projectpageview(request):
    top_data=topbar_tbl.objects.first()
    project_data=project_tbl.objects.all()

    return render(request,'project.html',{'project_data':project_data,'top_data':top_data})


def testimonialpageview(request):
    top_data=topbar_tbl.objects.first()
    testi_data=testi_tbl.objects.all()
    return render(request,'testimonial.html',{'testi_data':testi_data,'top_data':top_data})



def loginpageview(request):
    return render(request, 'login.html')




def loginpageview(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Django built-in authentication
        user = authenticate(request, username=username, password=password)

        if user is not None:     # Login Success
            login(request, user)
            return redirect('index')   # Home page ला redirect
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")





def videopageview(request):
   return render(request,"video.html")


