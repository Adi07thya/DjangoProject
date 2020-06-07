from django.contrib import admin
from .models import Customer,Bookmark,CustomerBookmark
# Register your models here.
@admin.register(Customer)
class AdminClass(admin.ModelAdmin):
    list_display=('id','latitude','longitude')


admin.site.register(Bookmark)
admin.site.register(CustomerBookmark)
