from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError


from lists.models import Item, List

def home_page(request):
    return render(request, "home.html")


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('/lists/%d/' % (list_.id,))

    return render(request, "list.html", {'list': list_})

def new_list(request):
    new_item_text = request.POST["item_text"]
    list_ = List.objects.create()
    try:
        item = Item(text=new_item_text, list=list_)
        item.save()
        item.full_clean()
    except ValidationError:
        error = "You can't have an empty list item"
        list_.delete()
        return render(request, 'home.html', {'error': error})
    return redirect('/lists/%d/' % (list_.id,))
