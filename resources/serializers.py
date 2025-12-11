from rest_framework import serializers
from .models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id','title','description','resource_type','url','file','created_by','created_at','updated_at','tags']
        read_only_fields = ['id','created_by','created_at','updated_at']

class ResourceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['title','description','resource_type','url','file','tags']

    def create(self, validated_data):
        user = self.context['request'].user
        resource = Resource.objects.create(
            created_by=user,
            **validated_data
        )
        return resource
