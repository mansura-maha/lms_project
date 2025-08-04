from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Category, Course
from .forms import CategoryForm, CourseForm

@staff_member_required
def category_list(request):
    categories = Category.objects.all()
    courses = Course.objects.all()
    return render(request, 'core/category/list.html', {
        'categories': categories,
        'courses': courses
    })

@staff_member_required
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'core/category/create.html', {'form': form})

@staff_member_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'core/category/update.html', {'form': form})

@staff_member_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'core/category/delete.html', {'category': category})

@staff_member_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'core/category/detail.html', {'category': category})

@staff_member_required
def course_list(request):
    courses = Course.objects.filter(is_active=True)
    return render(request, 'core/course/list.html', {'courses': courses})

@staff_member_required
def course_create(request):
    form = CourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        course = form.save(commit=False)
        course.save()
        form.save_m2m()
        return redirect('course_list')
    return render(request, 'core/course/create.html', {'form': form})

@staff_member_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid():
        course = form.save(commit=False)
        course.save()
        form.save_m2m()
        return redirect('course_list')
    return render(request, 'core/course/update.html', {'form': form})

@staff_member_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'core/course/delete.html', {'course': course})

@staff_member_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'core/course/detail.html', {'course': course})
