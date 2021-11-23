from django.contrib import admin
from students.models import Student

class Students(admin.ModelAdmin):
    list_display = ('id_student', 'name', 'nickname', 'phone')
    list_display_links = ('id_student', 'nickname')
    search_fields = ('nickname',)

admin.site.register(Student, Students)
