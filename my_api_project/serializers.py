# from rest_framework import models
from rest_framework import serializers

from django.db import models
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'url', 'language', 'price')