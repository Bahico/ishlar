from rest_framework import serializers
from .models import Task, Like, DisLike


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisLike
        fields = '__all__'
