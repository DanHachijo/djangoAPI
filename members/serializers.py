from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    # ForeginKeyはsourceで対応
    # office = serializers.CharField(source="office.name")
    #もしくはStringRelatedFieldで対応する
    office = serializers.StringRelatedField(many=False, read_only=True)
    # date = serializers.DateTimeField(format="%m/%d/%Y")

    class Meta:
        model = Member
        # fields = "__all__"
        # Activeスタッフしか出力しないのでStatusの項目をぬかしたものを出力
        fields = ["id", "office", "name", "email", "phone", "date"]
