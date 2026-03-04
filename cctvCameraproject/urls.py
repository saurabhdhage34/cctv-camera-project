"""
URL configuration for cctvCameraproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cameraapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('admin/', admin.site.urls),
    path('',views.homepageview,name="index"),
    path('index.html',views.homepageview,name="index"),
    path('about.html',views.aboutpageview,name="about"),
    path('feature.html',views.featurepageview,name="feature"),
    path('contact.html',views.contactpageview,name="contact"),
    path('quote.html',views.quotepageview,name="quote"),
    path('service.html',views.servicepageview,name="service"),
    path('team.html',views.teampageview,name="team"),
    path('subscribe/',views.subscribe_newsletter,name='subscribe_newsletter'),
    path('video.html',views.videopageview,name="video"),
    path('project.html',views.projectpageview,name="project"),
    path('testimonial.html',views.testimonialpageview,name="testimonial"),
    path('login/',views.loginpageview, name="login")


    
    


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)