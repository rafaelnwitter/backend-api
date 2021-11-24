from django.contrib import admin
from enrollments.models import Enrollment

class Enrollments(admin.ModelAdmin):
    list_display = ('id', 'score', 'status')
    list_display_links = ('id', 'score', 'status')
    search_fields = ('status',)

admin.site.register(Enrollment, Enrollments)
