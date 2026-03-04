from django.contrib import admin
from .models import contact_tbl,contact_map_tbl,quote_tbl,quote_img_tbl,topbar_tbl,index_tbl,testi_tbl,team_tbl,feature_tbl,feature_sub_tbl,project_tbl,service_tbl,about_tbl,about_sub_tbl,about_card_tbl

# Register your models here.

class admin_contact_tbl(admin.ModelAdmin):
     list_display=['u_name','u_email','u_subject','u_message']
admin.site.register(contact_tbl,admin_contact_tbl)


class admin_contact_map_tbl(admin.ModelAdmin):
     list_display=['mapp']
admin.site.register(contact_map_tbl,admin_contact_map_tbl)


class admin_quote_tbl(admin.ModelAdmin):
     list_display=['q_name','q_email','q_mo_no','q_select_ser','q_note']
admin.site.register(quote_tbl,admin_quote_tbl)


class admin_quote_img_tbl(admin.ModelAdmin):
     list_display=['img','q_title','q_info']
admin.site.register(quote_img_tbl,admin_quote_img_tbl)



class Admin_team_tbl(admin.ModelAdmin):
    list_display=['name','position','img','f_link','t_link','i_link']

admin.site.register(team_tbl,Admin_team_tbl)


class Admin_project_tbl(admin.ModelAdmin):
    list_display=['img','p_title','p_info','y_link','t_link']

admin.site.register(project_tbl,Admin_project_tbl)


class admin_service_tbl(admin.ModelAdmin):
     list_display=['img','s_title','s_info']
admin.site.register(service_tbl,admin_service_tbl)


class admin_about_tbl(admin.ModelAdmin):
     list_display=['img','a_title','a_info']
admin.site.register(about_tbl,admin_about_tbl)


class admin_about_sub_tbl(admin.ModelAdmin):
     list_display=['img','a_no','a_info']
admin.site.register(about_sub_tbl,admin_about_sub_tbl)


class admin_about_card_tbl(admin.ModelAdmin):
     list_display=['img','a_no','a_info','a_title']
admin.site.register(about_card_tbl,admin_about_card_tbl)


# class Admin_Testimonial_tbl(admin.ModelAdmin):
#     list_display=['name','img','message','profession']

# admin.site.register(Testimonial_tbl,Admin_Testimonial_tbl)

class admin_feature_tbl(admin.ModelAdmin):
     list_display=['img','f_title','f_info']
admin.site.register(feature_tbl,admin_feature_tbl)


class admin_feature_sub_tbl(admin.ModelAdmin):
     list_display=['img','f_title','f_info']
admin.site.register(feature_sub_tbl,admin_feature_sub_tbl)



class admin_testi_tbl(admin.ModelAdmin):
     list_display=['img','t_info','t_name','t_possion']
admin.site.register(testi_tbl,admin_testi_tbl)


class admin_index_tbl(admin.ModelAdmin):
     list_display=['h_img','h_title','h_p']
admin.site.register(index_tbl,admin_index_tbl)




class admin_topbar_tbl(admin.ModelAdmin):
     list_display=['address','top_email','top_mo','date']
admin.site.register(topbar_tbl,admin_topbar_tbl)




from .models import NewsletterSubscriber

admin.site.register(NewsletterSubscriber)






