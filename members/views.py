from django.shortcuts import render
from .models import Member
from .serializers import MemberSerializer
from rest_framework import viewsets


class MemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ReadOnlyのMemberデータの出力
    """
    queryset = Member.objects.all()
    # queryset = Member.objects.all()
    serializer_class = MemberSerializer
