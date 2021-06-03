from django.shortcuts import render  , get_object_or_404

# Create your views here.
from .models import *
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart , guestOrder
from .filters import ProductFilter





def store(request):
    products = Product.objects.all()
    myfilter = ProductFilter(request.GET, queryset=products)
    products = myfilter.qs

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created  = Order.objects.get_or_create(customer=customer , complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items


    else:
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_items': 0 , 'shipping': False}
        cartItems = order['get_cart_items']

        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}

       
        print('cart : ' , cart)
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']
                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quantity'])
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },

                'quantity': cart[i]['quantity'],
                'get_total': total,


            }
                items.append(item)
                if product.digital == False:
                    order['shipping'] = True
               


            except:
                pass

    context = {
        'products': products,
        'items': items,
        'order' : order ,
        'cartItems': cartItems,
        'myfilter':myfilter,
       
    }
    return render(request, 'store/store.html' , context)





  

def product_detail(request, id):
    product_detail = get_object_or_404(Product, id=id)

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created  = Order.objects.get_or_create(customer=customer , complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}

       
        print('cart : ' , cart)
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']
                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quantity'])
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },

                'quantity': cart[i]['quantity'],
                'get_total': total,


            }
                items.append(item)
                if product.digital == False:
                    order['shipping'] = True
               


            except:
                pass


    context = {
        'product_detail': product_detail,
        'items': items,
        'order' : order ,
        'cartItems': cartItems
    }

    return render(request, 'store/product_detail.html', context)
    

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created  = Order.objects.get_or_create(customer=customer , complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}

       
        print('cart : ' , cart)
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']
                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quantity'])
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },

                'quantity': cart[i]['quantity'],
                'get_total': total,


            }
                items.append(item)
                if product.digital == False:
                    order['shipping'] = True
               


            except:
                pass


    context = {
        'items': items,
        'order' : order ,
        'cartItems': cartItems
    }
    return render(request, 'store/cart.html' , context)




def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created  = Order.objects.get_or_create(customer=customer , complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    
    else:
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_items': 0 , 'shipping': False}
        cartItems = order['get_cart_items']

        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}

       
        print('cart : ' , cart)
        items = []
        order = {'get_cart_total' : 0 , 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']
                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quantity'])
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },

                'quantity': cart[i]['quantity'],
                'get_total': total,


            }
                items.append(item)
                if product.digital == False:
                    order['shipping'] = True
               


            except:
                pass
    context = {
        'items': items,
        'order' : order ,
        'cartItems': cartItems
    }
    return render(request, 'store/checkout.html' , context)





def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)




def process_order(request):

    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:
        print('user is not logged in .. ')
        print('cookies', request.COOKIES)

        customer, order = guestOrder(request, data)

#    regardless who checkout .., get the code below
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)