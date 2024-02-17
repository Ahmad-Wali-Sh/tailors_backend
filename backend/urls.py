from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('orders/total/', views.OrderViewSet.as_view(
        {'post': 'get_total_orders_and_prices'}), name='total_orders_prices'),
]
