from django.urls import path

from accounts.views import home, products, customers

app_name = 'accounts'
urlpatterns = [
    path('/', home, name='home'),
    path('/products', products, name='products'),
    path('/customers', customers, name='customers')
]
