
from rest_framework.response import Response
from django.shortcuts import render
from django.forms.models import model_to_dict
import json
from django.http import JsonResponse
from products.models import Product
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.


#Django Models 

@api_view(['POST'])
def api_home(request,*args,**kwargs):

    """
    DRF API View
    """
    serializer= ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"Invalid":"Not good "}, status=400)
    
    
 