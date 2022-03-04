# from cgitb import lookup
from rest_framework import serializers
from .models import Ticket, Category
from members.models import Member


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        # fields = ["id", "name"]


class TicketSerializer(serializers.ModelSerializer):
    #     title = serializers.CharField(max_length=100)
    # category = CategorySerializer(many=False, read_only=True)
    category = CategorySerializer()

    # category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
    # ストリングで表示したい場合
    # category = serializers.StringRelatedField(many=False, read_only=False)
    # Getリクエストの時だけでソースを表示したい場合
    # category = serializers.CharField()
    # staff = serializers.StringRelatedField(read_only=False, many=False)
    # staff = serializers.CharField(source="member.name")

    date = serializers.DateTimeField(format="%m/%d/%Y %H:%M:%S")
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
        # depth = 1

    # def create(self, validated_data):
    #     ticket_data = validated_data.pop('category')
    #     ticket = Ticket.objects.create(**validated_data)
    #     Ticket.objects.create(ticket=ticket, **ticket_data)
    #     return ticket

    # def create(self, validated_data):
    #     ticket_data = validated_data.pop('category')
    #     category_serializer = CategorySerializer(data=category)
    #     if category_serializer.is_valid():
    #         category_serializer.save()

    #     ticket = Ticket.objects.create(category=category_serializer.instance,
    #                                    **validated_data)
    #     return ticket
