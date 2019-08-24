from django.shortcuts import render,get_object_or_404
from .models import Category, Picture

# Create your views here.
def picture_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    pictures = Picture.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        pictures = pictures.filter(category=category)
    return render(request, 'gallery/picture/list.html',{'category': category,
                   'categories': categories,
                   'pictures': pictures})


def picture_detail(request, id, slug):
    picture = get_object_or_404(Picture,id=id,slug=slug)
    return render(request,'gallery/picture/detail.html',{'picture': picture})


