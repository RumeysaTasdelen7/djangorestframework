from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from ..models import Gazeteci, Makale
from .serializers import GazeteciSerializer, MakaleSerializer


class MakaleListCreateAPView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Makale.objects.filter(aktif=1)
    serializer = MakaleSerializer

    def perform_create(self, serializer):
        serializer.save()

class MakaleDetailAPIView(APIView):
    def get_object(self, pk):
        makale_instance = Makale.objects.get(pk=pk)
        return makale_instance
    
    def get(self, request, pk):
        makale = self.get_object(pk=pk)
        serializer = MakaleSerializer(makale)
        return Response(serializer.data)
    
    def put(self, request, pk):
        makale = self.get_object(pk=pk)
        serializer = MakaleSerializer(makale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        makale = self.get_object(pk=pk)
        makale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class GazeteciListCreateAPView(APIView):
    def get(self, request):
        gazeteciler = Gazeteci.objects.all()
        serializer = GazeteciSerializer(gazeteciler, many=1)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = GazeteciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GazeteciDetailAPIView(APIView):
    def get_object(self, pk):
        gazeteci_instance = Gazeteci.objects.get(pk=pk)
        return gazeteci_instance
    
    def get(self, request, pk):
        gazeteci = self.get_object(pk=pk)
        serializer = GazeteciSerializer(gazeteci)
        return Response(serializer.data)
    
    def put(self, request, pk):
        gazeteci = self.get_object(pk=pk)
        serializer = GazeteciSerializer(gazeteci, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        gazeteci = self.get_object(pk=pk)
        gazeteci.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)