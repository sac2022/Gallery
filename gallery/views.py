from django.shortcuts import render, redirect
from gallery.forms import ImageForm
from .filter import CategoryFilter
from .models import ImageModel


# Create your views here.
def index(request):
    cat_list = []
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "index.html", {"obj": obj})
    else:
        form = ImageForm()
    all_img = ImageModel.objects.all()
    print(request.GET.get('dropdown'))
    img = ImageModel.objects.filter(category=request.GET.get('dropdown')).order_by('date').reverse()
    for i in all_img:
        if i is not cat_list:
            cat_list.append(i.category)
            print(cat_list)
    if request.GET.get('dropdown') is None:
        return render(request, "index.html",{"all_img": all_img, "form": form, "cat_list": cat_list})
    else:
        return render(request, "index.html",{"img": img, "form": form,"cat_list":cat_list})