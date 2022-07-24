from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_all_items),
    path('insert_item/', views.insert_Items)
]
# http://127.0.0.1:8000/company/list/