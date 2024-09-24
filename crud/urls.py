from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('api/', views.items_list, name='items_list'),
    path('', views.items_list),  # You can map the home page to this view too
]