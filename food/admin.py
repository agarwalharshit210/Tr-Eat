from django.contrib import admin
from food.models import Contact
from food.models import Category, Sub_Category
from food.models import Customer
from food.models import Order
from food.models import OrderItem
from food.models import ShippingAddress
# from food_app.models import Register

# Register your models here.

admin.site.site_header = "Tr-Eat | Admin"


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email',
                    'subject', 'added_on', 'is_approved']


class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, Sub_CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
# admin.site.register(Regisster, RegisterAdmin)
