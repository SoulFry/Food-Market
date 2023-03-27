from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import *
from .forms import *
from cart.forms import CartAddProduct
from main.forms import CommentForm

def cafes(request):
    searchquery = request.GET.get('search', '')
    category = CafeCategory.objects.all()

    if searchquery:
        cafelist = Cafe.objects.filter(name__icontains=searchquery)
    else:
        cafelist = Cafe.objects.all()

    contex = {
        'cafes': cafelist,
        'categoryes': category,
    }

    return render(request, 'cafes-list.html', contex)

def cafemenu(request, name):
    cafe = Cafe.objects.get(name__iexact=name)
    cafe_menu = cafe.cafemenu_set.all()
    comments = cafe.commentcafe_set.all()
    categoryes = []
    for dish in cafe_menu:
        if dish.category not in categoryes:
            categoryes.append(dish.category)
    cart_add_form = CartAddProduct()
    comment_add_form = CommentForm()
    contex = {
        'cafe': cafe,
        'categoryes': categoryes,
        'cafemenu': cafe_menu,
        'cart_add_form': cart_add_form,
        'comment_add_form': comment_add_form,
        'comments': comments,
    }
    return render(request, 'cafe-menu.html', contex)

def cafeAdd(request):
    if request.method == 'POST':
        form = CafeAddForm(request.POST, request.FILES)
        if form.is_valid():
            category_choiced = form.cleaned_data['category']
            cafe = form.save(commit=False)
            cafe.category = category_choiced
            cafe.save()
            messages.success(request, 'Заведение успешно добавлено')
            form = CafeAddForm()
        else:
            messages.error(request, 'Заведение не удовлетворяет требованиям')
            form = CafeAddForm()
    else:
        form = CafeAddForm()
    return render(request, 'cafe-add.html', {'form': form})


def cafeMenuAdd(request, name):
    if request.method == 'POST':
        form = CafeMenuAddForm(request.POST, request.FILES)
        if form.is_valid():
            cafe = Cafe.objects.get(name=name)
            cafemenu = form.save(commit=False)
            cafemenu.id_cafe = cafe
            cafemenu.save() 
            messages.success(request, 'Блюдо успешно добавлено')
            form = CafeMenuAddForm()
        else:
            messages.error(request, 'Блюдо не удовлетворяет требованиям')
            form = CafeMenuAddForm()
    else:
        form = CafeMenuAddForm()
    return render(request, 'cafe-menu-add.html', {'form': form})


def comment_add(request, cafe):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_cafe = Cafe.objects.get(name=cafe)
            comment.from_user = request.user
            comment.save()
            print("Nice")
            return redirect('cafe-menu', name=cafe)

def edit_cost(request, product):
    product = CafeMenu.objects.get(id=product)
    from_cafe = product.id_cafe
    if request.method == 'POST':
        form = CafeMenuCostEdit(request.POST)
        if form.is_valid():
            product.cost = form.cleaned_data['cost']
            product.save()
            return redirect('cafe-menu', name=from_cafe)
        else:
            form = CafeMenuCostEdit()
    else:
        form = CafeMenuCostEdit
    return render(request, 'cafemenu-cost-edit.html', {'form': form})
