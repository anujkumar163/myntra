from rest_framework import serializers
from .models import Purcheger

class PurchegerSerializer(serializers.ModelSerializer):
	class meta():
		model = Purcheger
		fields = '__all__'