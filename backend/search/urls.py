from django.urls import path

from .views import SearchListView, OldSearchListView
urlpatterns = [
    path('',SearchListView.as_view(), name='search'),
    path('old/',OldSearchListView.as_view(), name='old-search'),
]