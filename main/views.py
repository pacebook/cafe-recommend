from django.shortcuts import render, render_to_response
# from django.http.response import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CafeSerializer
from .models import Cafe

def home(request):
    return render(request, template_name='main/base.html')

@api_view(['GET', 'POST'])
def api_cafe(request):
    if request.method == 'GET':
        cafes = Cafe.objects.all()
        serializer = CafeSerializer(cafes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CafeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #     title = request.POST.name
    #     desc = request.POST.desc
    #     # cafe = Cafe.objects.create(title=title, desc=desc)


    else:
        pass
    # elif request.method == '':
    #     flag = request.


@api_view(['GET'])
def api_cafe_detail(request, pk):
    cafe = Cafe.objects.get(pk=pk)
    serializer = CafeSerializer(cafe, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])

# @api_view((['GET']))
# def api_cafe_add(request):
#     flag = request.GET.get('flag')
#
#     if flag == str(1):
#         return Response(status=status.HTTP_200_OK)
#     else:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#



