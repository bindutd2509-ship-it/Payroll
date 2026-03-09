from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Designation
from .serializers import DesignationSerializer


# CREATE API
class CreateDesignationAPI(APIView):

    def post(self, request):
        serializer = DesignationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# LIST API
class ListDesignationAPI(APIView):

    def get(self, request):
        designations = Designation.objects.all()
        serializer = DesignationSerializer(designations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
