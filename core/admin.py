from django.contrib import admin
from .models import Category, Course

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'list_instructors', 'price', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'description']
    filter_horizontal = ['instructors']  

    def list_instructors(self, obj):
        return ", ".join([i.username for i in obj.instructors.all()])
    list_instructors.short_description = 'Instructors'
