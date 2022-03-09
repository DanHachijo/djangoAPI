# from cgitb import lookup
from rest_framework import serializers
from .models import Ticket, Category
from members.models import Member
from drf_writable_nested import WritableNestedModelSerializer

from members.serializers import MemberSerializer
from customers.serializers import StoreSerializer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        # fields = ["id", "name"]


class TicketSerializer(WritableNestedModelSerializer):
    category = CategorySerializer()
    staff = MemberSerializer()
    store = StoreSerializer()
    # category = serializers.StringRelatedField(many=False, read_only=False)
    # category = CategorySerializer(many=False, read_only=True)
    # category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
    # ストリングで表示したい場合
    # Getリクエストの時だけでソースを表示したい場合
    # category = serializers.CharField()
    # staff = serializers.StringRelatedField(read_only=False, many=False)
    # date = serializers.DateTimeField(format="%m/%d/%Y %H:%M")
    class Meta:
        model = Ticket
        fields = '__all__'
        # depth = 1

