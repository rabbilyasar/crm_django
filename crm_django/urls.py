from django.contrib import admin
from django.urls import path, include

from accounts.views import home, products, customers

# from accounts.urls import

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts', include('accounts.urls')),
    path('', home, name='home'),
    path('products', products, name='products'),
    path('customers', customers, name='customers')
]
