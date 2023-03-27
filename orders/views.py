from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage


from FoodSite import settings
from .models import *
from cart.cart import Cart
from cafes.models import *
from .forms import AdressSubmitForm


def checkout_order(request):
    cart = Cart(request)
    form = AdressSubmitForm()
    if request.method == 'POST':
        form=AdressSubmitForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cafes = []
            for item in cart:
                cafemenu = CafeMenu.objects.get(name=item['object'])
                get_cafe_id = cafemenu.id_cafe
                cafe = Cafe.objects.get(name=get_cafe_id)
                cafe_id = cafe.id
                if cafe_id not in cafes:
                    cafes.append(cafe_id)
            for cafe_id in cafes:
                cafe = Cafe.objects.get(id=cafe_id)
                cafe_email = cafe.email
                order = ''
                for item in cart:
                    cafemenu = CafeMenu.objects.get(name=item['object'])
                    get_cafe_id = cafemenu.id_cafe
                    cafe = Cafe.objects.get(name=get_cafe_id)
                    order_cafe_id = cafe.id
                    if cafe_id == order_cafe_id:
                        order += "Блюдо: " + cafemenu.name + ','
                        order += ' Количество: ' + str(item['count'])
                        order += ', '
                time = cd['time'].strftime("%B %d, %H:%M, %Y")
                order += '; Доставить до ' + time + ' года; '
                order += 'Адресс доставки: '+ cd['adress']
                email_subject = 'У вас новый заказ!'
                send_mail(
                    email_subject,
                    order,
                    settings.DEFAULT_FROM_EMAIL,
                    [cafe_email],
                    fail_silently=False)
            user_order = ''
            for item in cart:
                cafemenu = CafeMenu.objects.get(name=item['object'])
                user_order += "Блюдо: " + cafemenu.name + ','
                user_order += ' Количество: ' + str(item['count'])
                user_order += ', '
            user_order += '; Доставят до ' + time + ' года; '
            user_order += 'Адресс доставки: ' + cd['adress']
            user_email_subject = 'Ваш заказ'
            user = request.user
            send_mail(
                user_email_subject,
                user_order,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False)
            return redirect('orders:order-create')
    return render(request, 'order-create.html', {'cart': cart, 'form': form})


def create_order(request):
    cart = Cart(request)
    new_order = Order.objects.create(user=request.user)
    for item in cart:
        cafemenu = CafeMenu.objects.get(name=item['object'])
        cafe_id = cafemenu.id_cafe
        cafe = Cafe.objects.get(name=cafe_id)
        ItemsInOrder.objects.create(
            order=new_order,
            cafe=cafe,
            dish=cafemenu,
            count=item['count'],
            cost=item['cost'],
        )
    cart.clear()
    return redirect('orders:order-created')


def created_order(request):
    return render(request, 'order-created.html')
