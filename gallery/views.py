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
    print(request.GET.get('category'))
    img = ImageModel.objects.filter(category=request.GET.get('category')).order_by('date').reverse()
    for i in all_img:
        if i is not cat_list:
            cat_list.append(i.category)
            # print(cat_list)
    cat_list = set(cat_list)
    print(request.GET.get('Filter'))
    if request.GET.get('category') is None:
        return render(request, "index.html", {"all_img": all_img, "form": form, "cat_list": cat_list})
    elif request.GET.get('Filter') is None or request.GET.get('all'):
        return render(request, "index.html", {"img": img, "form": form, "cat_list": cat_list})
    else:
        return render(request, "index.html", {"all_img": all_img, "form": form, "cat_list": cat_list})
