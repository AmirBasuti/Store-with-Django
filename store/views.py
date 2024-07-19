# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view()
def product_list(request):
    # return HttpResponse("Hello, World!")
    return Response("Hello, World!")


@api_view()
def product_detail(request, id):
    return Response(id)
