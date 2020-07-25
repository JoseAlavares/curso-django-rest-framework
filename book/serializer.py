from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
	"""docstring for BookSerializer"""
	class Meta:
		model = Book
		fields = '__all__'