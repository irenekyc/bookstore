from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=500)
    price = serializers.IntegerField()
    rating = serializers.IntegerField()
    num_reviews = serializers.IntegerField()
    category = serializers.CharField()
    availablility = serializers.BooleanField()
    thumbnail = serializers.CharField()
