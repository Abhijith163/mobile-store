from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView,CreateView,UpdateView,DeleteView

from customer.models import MyOrders, OrderItems
from .forms import *
from django.urls import reverse_lazy
from .models import *
from django.db.models import Q

# Create your views here.
class SHome(TemplateView):
    template_name="storehome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Mobile.objects.filter(user=self.request.user).order_by('-datetime')
        return context
    
    
def add_mob(request):
    if request.method == 'POST':
        form = MobForm(request.POST, request.FILES)
        if form.is_valid():
            mob = form.save(commit=False)
            mob.user = request.user
            mob.save()
            return redirect('sh')
    else:
        form = MobForm()
    return render(request, 'addmob.html', {'form': form})
    
class Edit_mob(UpdateView):
    form_class=MobForm
    template_name="editmob.html"
    model=Mobile
    success_url=reverse_lazy("sh")
    pk_url_kwarg="pk"
    
class Delete_mob(DeleteView):
    model=Mobile
    template_name="deletemobile.html"
    success_url=reverse_lazy("sh")
    
    
class Pro(TemplateView):
    template_name="storeprofile.html"
    
    
class Edit_prof(UpdateView):
    form_class=MobForm
    template_name="editprofile.html"
    success_url=reverse_lazy("prof")
    pk_url_kwarg="pk"
    
    
def orders(request):
    order_items = OrderItems.objects.filter(product__user=request.user).all()
    order_ids = OrderItems.objects.filter(product__user=request.user).values()
    ids = []
    for i in order_ids:
        ids.append(i['order_id'])
        
    ids = list(set(ids))
    orders = MyOrders.objects.filter(id__in=ids).all()

    context = {
        "orders": orders,
        "order_items": order_items,
    }
    return render(request, "order.html", context)
    

def searchhhh(request):
    key = request.GET.get('key', '')
    products = Mobile.objects.filter(Q(brand__icontains=key) | Q(model__icontains=key)).all() 
    context = {
        'data': products,
    }
    return render(request, "searchStore.html", context)
    