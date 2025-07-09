from django.contrib import admin
from school.models import Student, Course, Enrollment

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

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enrollment_date', 'period')
    list_display_links = ('id',)
    list_per_page = 20

admin.site.register(Student, StudentAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Course, CourseAdmin)
