from django.urls import path
from .views import MemberList
urlpatterns = [
    path('', MemberList.as_view()),
]
