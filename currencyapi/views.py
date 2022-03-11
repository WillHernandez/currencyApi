from django.http import JsonResponse
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def currency_list(request, format=None):

	if request.method == 'GET':
		# get all the drinks
		currencies = Currency.objects.all()
		# serialize them
		serializer = CurrencySerializer(currencies,many=True)
		# return json
		return Response(serializer.data)

	if request.method == 'POST':
		serializer = CurrencySerializer(data=request.data)	
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def currency_detail(request, id, format=None):
	try:
		currency = Currency.objects.get(pk=id)	
	except Currency.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		serializer = CurrencySerializer(currency)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = CurrencySerializer(currency, data=request.data)	
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, stats=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		currency.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)