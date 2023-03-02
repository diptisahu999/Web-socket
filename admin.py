from django.contrib import admin
from .models import Student,Job

# Register your models here.
admin.site.register(Student)
# admin.site.register(Job)
@admin.register(Job)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','job','salary']

