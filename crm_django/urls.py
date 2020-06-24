from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

from accounts.views import registerPage, loginPage, logoutUser, home, userPage, products, customers, createCustomerOrder, updateOrder, deleteOrder, accountSettings

urlpatterns = [

    path('admin/', admin.site.urls),

    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('', home, name='home'),
    path('user/', userPage, name='user_page'),

    path('account/', accountSettings, name="account"),

    path('products/', products, name='products'),
    path('customer/<str:pk>', customers, name='customer'),

    path('create_order/<str:pk>', createCustomerOrder,
         name="customer_create_order"),
    path('update_order/<str:pk>', updateOrder, name="update_order"),
    path('delete_order/<str:pk>', deleteOrder, name="delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/password_reset_sent.html', auth_views.PasswordResetDoneView.as_view(template_name="accounts/"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
