from django.urls import path

from . import views

urlpatterns = [
    # path("list/",views.ProductListAPIView.as_view(),name='product-list'),
    path("",views.product_alt_view,name='product-list-create'), #the same view can handle both get and create
    path("<int:pk>",views.product_alt_view,name='product-detail'),
]
