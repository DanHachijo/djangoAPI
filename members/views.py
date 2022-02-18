from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView
from .models import Members
from .serializers import MembersSerializer


class MemberList(APIView):
    def get(self, request, format=None):
        members = Members.objects.all()
        serializer = MembersSerializer(members, many=True)
        return Response(serializer.data)
