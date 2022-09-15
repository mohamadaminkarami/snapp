from rest_framework import generics
from authentication import serializers


class RegisterCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
