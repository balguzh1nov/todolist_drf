from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


# Create your views here.

@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/task-list/",
        "Details": "/details/<str:pk>",
        "Create": "/create/",
        "Update": "/update/<str:pk>",
        "Delete": "/delete/<str:pk>",
    }

    return Response(api_urls)


@api_view(["GET"])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def details(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)


@api_view(["POST"])
def create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item successfully deleted")