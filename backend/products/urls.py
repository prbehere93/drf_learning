from django.urls import path

from . import views

urlpatterns = [
    path("create/",views.ProductCreateAPIView.as_view(),name='product-create'),
    path("<int:pk>",views.ProductAPIView.as_view(),name='product-detail'),
]
