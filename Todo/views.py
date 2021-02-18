from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import TodoModel

class TodoView(generics.CreateAPIView):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()

class TodoListView(generics.GenericAPIView):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()

    def get(self, request):
        lst = TodoModel.objects.all()
        serializer = self.serializer_class(lst, many=True)
        unarchive_list = []
        for item in serializer.data:
            if item["archive"] is False:
                unarchive_list.append(item)
        return Response(unarchive_list,
        status=status.HTTP_200_OK)

class TodoShowView(generics.GenericAPIView):

    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()

    def get(self, request, id):
        lst = TodoModel.objects.filter(id=id)
        serializer = self.serializer_class(lst, many=True)
        return Response(serializer.data,
        status=status.HTTP_200_OK)

class TodoDelete(generics.GenericAPIView):

    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()

    def delete(self, request, id):
        try:
            TodoModel.objects.get(id=id).delete()
            return Response("Deleted Succefully.",
            status=status.HTTP_202_ACCEPTED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class TodoUpdate(generics.GenericAPIView):

    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()

    def put(self, request, id):
        lst = TodoModel.objects.get(id=id)
        serializer = self.serializer_class(lst, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
            status=status.HTTP_200_OK)

        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)

class TodoArchiveList(generics.GenericAPIView):

    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()

    def get(self, request):
        lst = TodoModel.objects.all()
        serializer = self.serializer_class(lst, many=True)
        archive_list = []
        for item in serializer.data:
            if item["archive"] is True:
                archive_list.append(item)
        return Response(archive_list,
        status=status.HTTP_200_OK)