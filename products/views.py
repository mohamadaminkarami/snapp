from rest_framework import generics
from rest_framework import permissions
from products import mixins
from products import serializers


class ProductScoreCreateAPIView(mixins.CreateListModelMixin, generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ProductScoreSerializer
