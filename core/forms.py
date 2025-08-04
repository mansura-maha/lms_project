from django import forms
from django.contrib.auth.models import User
from .models import Category, Course

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'is_active']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'banner',
            'price',
            'duration',
            'category',
            'instructors',
            'is_active'
        ]
        widgets = {
            'instructors': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['instructors'].queryset = User.objects.filter(is_staff=True)
