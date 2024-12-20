"""
URL configuration for MyFood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from food import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact_us,name="contact"),
    path('feature/',views.feature,name="feature"),
    path('menu/',views.menu,name="menu"),
    path('order/',views.order,name="order"),
    path('registration/',views.signpage,name="registration"),
    path('login/',views.Login_page,name="login"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('process_order/',views.processOrder,name="process_order"),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
