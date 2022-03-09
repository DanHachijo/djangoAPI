from rest_framework import serializers
from .models import Member, Office
from drf_writable_nested import WritableNestedModelSerializer


# class OfficeSerializer(WritableNestedModelSerializer):
#     class Meta:
#         model = Office
#         fields = ["id", "name"]


class MemberSerializer(WritableNestedModelSerializer):
    # office = OfficeSerializer()
    # ForeginKeyはsourceで対応
    # office = serializers.CharField(source="office.name")
    # もしくはStringRelatedFieldで対応する
    # office = serializers.StringRelatedField(many=False, read_only=True)
    # date = serializers.DateTimeField(format="%m/%d/%y %H:%M")

    class Meta:
        model = Member
        # fields = "__all__"
        # Activeスタッフしか出力しないのでStatusの項目をぬかしたものを出力
        fields = ["id", "name"]
