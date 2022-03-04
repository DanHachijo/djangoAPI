from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):
    # ForeginKeyはsourceで対応
    # company = serializers.CharField(source="company.name")
    # name = serializers.CharField(max_length=30)
    # street = serializers.CharField(max_length=100)
    # suite = serializers.CharField(max_length=100)
    # city = serializers.CharField(max_length=100)
    # State = serializers.CharField(max_length=100)
    # zipcode = serializers.IntegerField()
    # status = serializers.CharField()
    # contact = serializers.CharField(max_length=30)
    # phone = serializers.IntegerField()
    # email = serializers.EmailField()
    # date = serializers.DateTimeField(format="%m/%d/%Y")

    class Meta:
        model = Store
        fields = '__all__'
# many-to-manyの場合
    # tags = serializers.StringRelatedField(read_only=True, many=True)
