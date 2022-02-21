from cgitb import lookup
from rest_framework import serializers
from .models import Ticket, Category

class CategorySerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField()

    class Meta:
        model = Category
        fields = "__all__"      

class TicketSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=100)
#     category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
#ストリングで表示したい場合
#     category = serializers.StringRelatedField(many=False, read_only=False)
# Getリクエストの時だけでソースを表示したい場合
#     category = serializers.CharField(source="category.name")
#     staff = serializers.PrimaryKeyRelatedField(many=False, queryset=Member.objects.all())

#     date = serializers.DateTimeField()
#     urgent = serializers.BooleanField()
#     status = serializers.CharField(max_length=100)
#     inquery = serializers.CharField(max_length=1000)
#     respond = serializers.CharField(max_length=1000)
#     store = serializers.PrimaryKeyRelatedField(many=False, queryset=Store.objects.all())

#     contact_name = serializers.CharField(max_length=100, default="Staff")
#     email = serializers.EmailField(max_length=100)
#     phone = serializers.CharField(max_length=100)
#     escalated = serializers.BooleanField()

    class Meta:
        model = Ticket
        fields = '__all__'

# many-to-manyの場合
        # language = serializers.StringRelatedField(read_only=True, many=True)
