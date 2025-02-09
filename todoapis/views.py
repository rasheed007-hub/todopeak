from rest_framework.views import APIView
from rest_framework import status, serializers
from rest_framework.response import Response

from .serializers import TodoSerializer
from .models import Todo
# Create your views here.

class TodoView(APIView):
    def get(self, request):
        try:
            todo = Todo.objects.all()
            serializer = TodoSerializer(todo, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Message" :str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
       try:
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       except Exception as e:
            return Response({"Message" :str(e)}, status=status.HTTP_400_BAD_REQUEST)
       

class TodoDetailView(APIView):
    def get(self,request, id):
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Message" : str(e)}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Message" : str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id): 
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({"Message" : "Todo deleted successfuly"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"Message" : str(e)}, status=status.HTTP_404_NOT_FOUND)