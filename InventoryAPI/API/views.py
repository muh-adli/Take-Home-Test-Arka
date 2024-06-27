## Django and DRF core
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.core.serializers import serialize
from xml.etree.ElementTree import Element, SubElement, tostring
from rest_framework import viewsets
from rest_framework.response import Response


## models and serializers
from .models import Product
from .serializer import ProductSerializer

## Library
from datetime import datetime

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def inventoryJson(request):
    start = datetime.now()
    products_qs = Product.objects.values('product_id', 'product_name', 'description', 'price')
    end = datetime.now()
    delta = end - start
    print("Inventory JSON qs: ", round(delta.total_seconds(), 3), "s")
    return JsonResponse(list(products_qs), safe=False)

class inventoryRest(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        start = datetime.now()
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        end = datetime.now()
        delta = end - start
        print("Inventory REST qs: ", round(delta.total_seconds(), 3), "s")
        return Response(serializer.data)

def inventoryXml(request):
    start = datetime.now()
    products_qs = Product.objects.all()

    root = Element('products')
    for product in products_qs:
        product_element = SubElement(root, 'product')
        SubElement(product_element, 'product_id').text = str(product.product_id)
        SubElement(product_element, 'product_name').text = product.product_name
        SubElement(product_element, 'description').text = product.description
        SubElement(product_element, 'price').text = str(product.price)
    
    xml_string = tostring(root, encoding='utf-8').decode('utf-8')
    end = datetime.now()
    delta = end - start
    print("Inventory XML qs: ", round(delta.total_seconds(), 3), "s")
    return HttpResponse(xml_string, content_type='application/xml')