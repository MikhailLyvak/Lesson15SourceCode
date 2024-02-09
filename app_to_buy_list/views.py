from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
import datetime
from django.db.models import Sum

from .models import Item, ItemType

def index(request):
    num_item_types = ItemType.objects.count()
    num_item = Item.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_item": num_item,
        "num_item_types": num_item_types,
        "num_visits": num_visits + 1
    }

    return render(request, "app_to_buy_list/index.html", context=context)


class ItemListView(generic.ListView):
    model = Item
    template_name = "app_to_buy_list/item_list.html"
    context_object_name = "item_list"
    
    def get_queryset(self):
        return Item.objects.select_related("item_type")
    
    def get_context_data(self, *args, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        
        context["total_sum"] = Item.objects.aggregate(total_price=Sum('price'))['total_price']
        context["total_amount"] = Item.objects.count()
        
        return context
    

class ItemCreateView(generic.CreateView):
    model = Item
    template_name = 'app_to_buy_list/create_item.html'
    fields = ["name", "discription", "price", "item_type", "link"]
    success_url = reverse_lazy('app_to_buy_list:item-list')

    def form_valid(self, form):
        item = form.save(commit=False)

        if item.item_type.name == "PK Types":
            item.price_in_future = int(item.price * 0.8)

        item.save()

        return super().form_valid(form)

class ItemUpdateView(generic.UpdateView):
    model = Item
    template_name = 'app_to_buy_list/update_item.html'
    fields = ["name", "discription", "price", "item_type", "link"]
    success_url = reverse_lazy('app_to_buy_list:item-list')
    
    
class ItemDetailView(generic.DetailView):
    model = Item
    template_name = "app_to_buy_list/item_detail.html"
    context_object_name = "item"
    
    def get_queryset(self):
        return Item.objects.select_related("item_type")
    

def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect(reverse("app_to_buy_list:item-list"))    

def mark_item_as_bought(request, pk):
    item = Item.objects.get(pk=pk)
    item.is_bought = True
    item.bought_date = datetime.date.today()
    item.save()
    return redirect(reverse("app_to_buy_list:item-list"))
