from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , related_name='customer', blank=True, null=True)
    name = models.CharField( max_length=50 , blank=True, null=True)
    email = models.EmailField( max_length=254)

    

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

 


SIZE_CHOICES = (
    ('LG' , 'Large'),
    ('MD' , 'Medium'),
    ('SM', 'Small'),
)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.TextField(choices=SIZE_CHOICES , max_length=100 , default='Medium' ,  blank=True, null=True)
    digital = models.BooleanField(default=False , blank=True, null=True)
    image = models.ImageField( blank=True, null=True)
    desc = models.TextField(max_length=1000 ,  default="Fashion is part of the daily air and it changes all the time.")
 


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"id": self.id})



class Order(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.SET_NULL , blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id =  models.CharField(max_length=100 ,  null=True)
    

    

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems ])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems ])
        return total


    

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL  , null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL  , null=True)
    quantity = models.IntegerField(default=0 , blank=True, null=True)
    date_added = models.DateTimeField( auto_now_add=True)

    

    class Meta:
        verbose_name = _("OrderItem")
        verbose_name_plural = _("OrderItems")

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total





class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL  , null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL  , null=True)
    address =  models.CharField(max_length=200,  null=False)
    city = models.CharField(max_length=200,  null=False)
    state = models.CharField(max_length=200,  null=False)
    zipcode = models.CharField(max_length=200,  null=False)
    date_added = models.DateTimeField( auto_now_add=True)
    

    class Meta:
        verbose_name = _("ShippingAddress")
        verbose_name_plural = _("ShippingAddresss")

    def __str__(self):
        return self.address