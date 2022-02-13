from django.contrib import admin
from .models import Form1
# Register your models here.
class MyAdminSite(admin.AdminSite):
    site_header = 'Form1'
    site_title = 'Form1'
    index_title = 'Form1'
admin_site = MyAdminSite(name='myadmin')
admin_site.register(Form1)