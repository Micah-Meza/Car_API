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