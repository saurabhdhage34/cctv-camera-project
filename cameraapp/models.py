from django.db import models


# Create your models here.

class contact_tbl(models.Model):
    u_name=models.CharField(max_length=100)
    u_email=models.EmailField()
    u_subject=models.CharField(max_length=100)
    u_message=models.CharField(max_length=100)

class contact_map_tbl(models.Model):
    mapp=models.CharField(max_length=500)


class quote_tbl(models.Model):
    q_name=models.CharField(max_length=100)
    q_email=models.EmailField()
    q_mo_no=models.BigIntegerField()
    q_select_ser=models.CharField(max_length=100)
    q_note=models.CharField(max_length=100)

class quote_img_tbl(models.Model):

    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    q_title=models.CharField(max_length=100)
    q_info=models.CharField(max_length=100)
   


class team_tbl(models.Model):
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    f_link=models.CharField(max_length=100)
    t_link=models.CharField(max_length=100)
    i_link=models.CharField(max_length=100)


class project_tbl(models.Model):

    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    p_title=models.CharField(max_length=100)
    p_info=models.CharField(max_length=100)
    y_link=models.CharField(max_length=100)
    t_link=models.CharField(max_length=100)


class service_tbl(models.Model):

    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    s_title=models.CharField(max_length=100)
    s_info=models.CharField(max_length=100)
   


class about_tbl(models.Model):

    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    a_title=models.CharField(max_length=100)
    a_info=models.CharField(max_length=100)
   

class about_sub_tbl(models.Model):

    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    a_no=models.IntegerField()
    a_info=models.CharField(max_length=100)
   


class about_card_tbl(models.Model):

    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    a_no=models.IntegerField()
    a_title=models.CharField(max_length=100)
    a_info=models.CharField(max_length=100)

# class Testimonial_tbl(models.Model):
#     img=models.ImageField(upload_to="static/img",null=True,default=None)
#     message=models.CharField(max_length=200)
#     name=models.CharField(max_length=200)
#     profession=models.CharField(max_length=200)


class feature_tbl(models.Model):

    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    f_title=models.CharField(max_length=100)
    f_info=models.CharField(max_length=100)
   


class feature_sub_tbl(models.Model):

    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    f_title=models.CharField(max_length=100)
    f_info=models.CharField(max_length=100)



class testi_tbl(models.Model):
    img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    t_info=models.CharField(max_length=200)
    t_name=models.CharField(max_length=100)
    t_possion=models.CharField(max_length=100)

class index_tbl(models.Model):
    h_img=models.ImageField(upload_to="static",max_length=300,null=True,default=None)
    h_title=models.CharField(max_length=200)
    h_p=models.CharField(max_length=400)
   

class topbar_tbl(models.Model):
    address=models.CharField(max_length=300)
    top_email=models.EmailField()
    top_mo=models.BigIntegerField()
    date=models.CharField(max_length=200)



class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



from django.db import models

class OTP(models.Model):
    phone = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)





    

    

   



    