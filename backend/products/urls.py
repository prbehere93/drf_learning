from django.urls import path

from . import views

urlpatterns = [
    # path("list/",views.ProductListAPIView.as_view(),name='product-list'),
    path("",views.ProductListCreateAPIView.as_view(),name='product-list-create'), #the same view can handle both get and create
    path("<int:pk>/update/",views.ProductUpdateAPIView.as_view(),name='product-update'),
    path("<int:pk>/delete/",views.ProductDeleteAPIView.as_view(),name='product-delete'),
    path("<int:pk>",views.ProductAPIView.as_view(),name='product-detail'),
]
