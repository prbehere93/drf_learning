from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>",views.ProductAPIView.as_view(),name='product-detail'),
]
