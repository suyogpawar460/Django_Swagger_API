# from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactSerializer


# from .models import Contact


# Create your views here.

class SendEmail(APIView):
    # permission class set to be unauthenticated
    permission_classes = (permissions.AllowAny,)

    # this is where the drf-yasg gets invoked
    @swagger_auto_schema(request_body=ContactSerializer)
    def post(self, request):
        # serializer object
        serializer = ContactSerializer(data=request.data)
        # checking for errors
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
