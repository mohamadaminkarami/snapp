from rest_framework import serializers

from products.models import ProductScore


class ProductScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductScore
        fields = ['product', 'score']

    def validate(self, attrs):
        customer = self.context["request"].user
        if ProductScore.objects.filter(customer=customer, product=attrs['product']).exists():
            raise serializers.ValidationError(
                {'error': 'product score for the user exists'})

        return attrs

    def create(self, validated_data):
        customer = self.context["request"].user
        return super().create({**validated_data, 'customer': customer})
