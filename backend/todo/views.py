from .models import Todo
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
import traceback


# Create your views here.
@api_view(['GET', 'POST'])
def get_all_or_create(request):
    try:
        if request.method == 'GET':
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception:
        traceback.print_exc()
        return Response({ 'error':'500 INTERNAL SERVER ERROR' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def get_one_edit_delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        serializer: TodoSerializer
        if request.method == 'GET':
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            serializer = TodoSerializer(todo)
            todo.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        traceback.print_exc()
        return Response({ 'error':'500 INTERNAL SERVER ERROR' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def is_done(request, id):
    try:
        todo = Todo.objects.get(id=id)
        serializer: TodoSerializer
        todo.is_done = not todo.is_done
        todo.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception:
        traceback.print_exc()
        return Response({ 'error':'500 INTERNAL SERVER ERROR' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


