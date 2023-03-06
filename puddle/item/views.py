from django.shortcuts import redirect, render, get_object_or_404
#We import the Item database model from the models.py in items folder
from django.db.models import Q
from .models import Category, Item
from .forms import EditItemForm, NewItemForm
from django.contrib.auth.decorators import login_required

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if query:
        items = items.filter(Q(name__contains=query) or Q(description__icontains=query))

    if category_id:
        items=items.filter(category_id=category_id)

    return render(request, 'item/items.html', {
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id),
    })

def detail(request, pk):
    '''
    This returns the detail.html page to show the item details
    '''
    #we store single item object from database into a variable where pk=pk
    item = get_object_or_404(Item, pk=pk)
    #We store list of items with the same category as 'item' into related items
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        #With the page we return the list of items and related items
        'item':item,
        'related_items':related_items
    })

@login_required
def new(request):

    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form':form,
        'title': 'New Item'  
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request, pk):

    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form':form,
        'title': 'Edit Item'  
    })