from django.shortcuts import get_object_or_404 # a shortcut to help with shortening the code 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CarSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        # This is a lot of code soo to simplify we can write it as the above elif statements. 
            # if serializer.is_valid() == True:
            #     serializer.save()
            #     return Response(serializer.data, status = status.HTTP_201_CREATED)
            # else:
            #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
# make sure the pk request/parameter matches the urls app parameter for get by id function. 
def car_detail(request, pk): 

# Instead of all this code try using the statments below.
    # try:
    #     car = Car.objects.get(pk = pk)
    #     serializer = CarSerializer(car)
    #     return Response(serializer.data)

    # except Car.DoesNotExist:
    #     return Response(status = status.HTTP_404_NOT_FOUND)

#############################################################################################################################################

    # if request.method == 'GET':
    #     car = get_object_or_404(Car, pk = pk) # 2 arguments are needed which is the Model where its querying from and the pk = pk
    #     serializer = CarSerializer(car)
    #     return Response(serializer.data)

    # elif request.method == 'PUT':
    #     car = get_object_or_404(Car, pk = pk)
    #     serializer = CarSerializer(car, data = request.data)
    #     serializer.is_valid(raise_exception = True)
    #     serializer.save()
    #     return Response(serializer.data)

#############################################################################################################################################

# The above code can be trimmed down to this:

    car = get_object_or_404(Car, pk = pk)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
