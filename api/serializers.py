#just like forms

#importing serializer from drf
from rest_framework import serializers
from .models import Task

#name = model + serializer
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'