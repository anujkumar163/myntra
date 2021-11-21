from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Purcheger 
from .serializers import  PurchegerSerializer 
from rest_framework import status 

# Create your views here.

class PurchegerApiView(APIView):
	def get(self, request, pk=None):
		eobjs=Purcheger.objects.all()
		empJSON = PurchegerSerializer(eobjs, many=True)
		return Response({'data': empJSON.data})

	def post(self, request):
		empser = PurchegerSerializer(data=request.data)
		print(empser)
		if empser.is_valid():
			empser.save()
			return Response({'msg':'data received'}, status.HTTP_200_OK)
		else:
			return Response(empser.error, status.HTTP_400_BAD_REQUEST)	   
#-----------------------------------------------------------------------------------#
'''def put(self, request, pk):
	id=pk
	stu = Purcheger.objects.get(pk=id)
	serializer = PurchegerSerializer(stu, data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({'msg': 'Complete Update'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	    

def delete(self, request, pk, format=None):
	id = pk 
	stu = Purcheger.objects.get(pk=id)
	stu.delete()
	return Response({'msg': 'Data deleted'})'''