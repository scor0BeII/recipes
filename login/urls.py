from django.urls import path
from .views import index, who_are_you, recps, forms

urlpatterns = [
    path('', index, name = 'main'),
    path('ck', who_are_you, name = 'secret'),
    path('rc', recps, name = 'recipes'),
    path('tb', forms, name = 'table_entry'),

]
