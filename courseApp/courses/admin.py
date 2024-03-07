from django.contrib import admin
from django.utils.html import mark_safe
from courses.models import Category, Course
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'active']
    search_fields = ['name', 'drescription']
    list_filter = ['id', 'name']
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, course):
        if course.image:
            return mark_safe(f"<img width='200' src='/static/{course.image.name}' />")

    class Media:
        css = {
            'all': ['/static/css/style.css']

        }

admin.site.register(Category)
admin.site.register(Course, CourseAdmin)

