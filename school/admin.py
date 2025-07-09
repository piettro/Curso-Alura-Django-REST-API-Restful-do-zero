from django.contrib import admin
from school.models import Student, Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_birth', 'email', 'cpf', 'phone_number')
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name', 'email', 'cpf', 'phone_number',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description')
    list_display_links = ('id', 'code',)
    list_per_page = 20
    search_fields = ('code',)

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
