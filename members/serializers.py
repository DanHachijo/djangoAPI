from rest_framework import serializers
from .models import Members


class MembersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=60)
    phone = serializers.IntegerField()
    date = serializers.DateTimeField()

    class Meta:
        model = Members
        # fields = ['name', 'email', 'phone', 'date']
        fields = '__all__'
