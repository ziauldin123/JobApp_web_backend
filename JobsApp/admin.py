from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
	# fields = ('title','description','location','type','category','last_date','company_name','company_description','website','created_at','filled','salary','required_exp')
    list_display = ('title','description','location','type','category','last_date','company_name','company_description','website','created_at','filled','salary','required_exp')

admin.site.register(Job,JobAdmin)
	
		
		 