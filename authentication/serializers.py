from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    repeated_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'repeated_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['repeated_password']:
            raise serializers.ValidationError(
                {'password': 'Passwords did not match!'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
