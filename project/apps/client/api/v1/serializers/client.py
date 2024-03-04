from rest_framework import serializers

from apps.client.models import ClientCategory


class ClientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCategory
        fields = (
            'id', 'category', 'email', 'first_name', 'last_name', 'birth_date', 'gender',
        )
