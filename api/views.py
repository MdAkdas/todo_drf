from django.shortcuts import render
from django.http import JsonResponse
#importing model
from .models import Task

#for drf response and api_view (imp for drf)
from rest_framework.decorators import api_view
from rest_framework.response import Response

#importing from serializers 
from .serializers import TaskSerializer


# Create your views here.

@api_view(['GET']) #decorator
def apiOverview(request):
	api_urls = {
		'List': '/task.list/',
		'Detail View': '/task-detail/<str:pk>/',
		'Create': '/task-create/',
		'Update': '/task-update/<str:pk>/',
		'Delete': '/task-delete/str:pk>',
	}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	task = Task.objects.all()
	serializer = TaskSerializer(task,many=True) #serialize one or many
	return Response(serializer.data)	

@api_view(['GET'])
def taskDetail(request,pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(task,many=False) #serialize one or many
	return Response(serializer.data)	

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data) #serialize one or many

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)		

@api_view(['POST'])
def taskUpdate(request,pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data) #serialize one or many

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)	

@api_view(['DELETE'])
def taskDelete(request,pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response("Item deleted succesfuly")	