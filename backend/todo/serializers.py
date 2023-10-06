from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ["id","title", "description", "is_done", "date_created"]
