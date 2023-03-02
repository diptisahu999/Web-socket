from django.urls import path
from .import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('show/',views.show,name='show'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),

]
