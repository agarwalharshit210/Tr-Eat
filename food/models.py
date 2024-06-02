from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    image = models.ImageField(upload_to='img/', default='select image')
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

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
         total = sum([item.get_total for item in orderitems])
         return total
    
    @property
    def get_cart_items(self):
      orderitems = self.orderitem_set.all()
      total = sum([item.quantity for item in orderitems])
      return total



class Meta:
    db_table = 'customer'


class OrderItem(models.Model):
    product = models.ForeignKey(
        Sub_Category, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    # customer = models.ForeignKey(
    #     Customer, on_delete=models.SET_NULL, blank=True, null=True)
    # order = models.ForeignKey(
    #     Order, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(default='')
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
