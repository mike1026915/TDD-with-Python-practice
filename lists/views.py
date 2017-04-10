from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item, List

def home_page(request):
    return render(request, "home.html")


def view_list(request):
    items = Item.objects.all()
    return render(request, "list.html", {'items': items})

def new_list(request):
    new_item_text = request.POST["item_text"]
    list_ = List.objects.create()
    Item.objects.create(text=new_item_text, list=list_)
    return redirect('/lists/the-only-list-in-the-world/')