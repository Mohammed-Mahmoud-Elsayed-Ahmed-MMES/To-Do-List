from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

def base(request) :
    return render(request, 'base.html')

def index(request):
    return render(request, 'crud/index.html')


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def item_list_view(request):
    items = Item.objects.all().order_by('id')
    return render(request, 'item_list.html', {'items': items})

def delete_item(request, item_id):
    # Delete the item
    item_to_delete = get_object_or_404(Item, id=item_id)
    item_to_delete.delete()

    # Renumber the remaining items
    all_items = Item.objects.all().order_by('id')
    for i, item in enumerate(all_items):
        item.id = i + 1
        item.save()

    return redirect('todo_list')  # Adjust the redirect as needed for your app

@api_view(['GET', 'POST'])
@csrf_exempt  # This line disables CSRF protection (if needed for the API view)
def items_list(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = request.data
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Ensure proper permissions

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

