from django.contrib import admin
from courses.models import Course

class Courses(admin.ModelAdmin):
    list_display = ('id_course', 'name', 'description', 'duration')
    list_display_links = ('id_course', 'name')
    search_fields = ('name',)

admin.site.register(Course, Courses)
