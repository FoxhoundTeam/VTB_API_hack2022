import base64
from base64 import b64decode
import json

from dataclasses import Field
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, ReadOnlyField
from rest_framework.serializers import PrimaryKeyRelatedField, SlugRelatedField
from django.http import HttpRequest

from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'