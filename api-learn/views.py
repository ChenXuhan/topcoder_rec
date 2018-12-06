from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET', 'POST'])
def userDetail(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        instance = User.objects.get(username=username)
        serializer = UserSerializer(instance, context=serializer_context)
        print(serializer.data)
        return Response(serializer.data)
    if request.method == 'POST':
        username = request.POST['username']
        instance = User.objects.get(username=username)
        serializer = UserSerializer(instance, context=serializer_context)
        print(serializer.data)
        return Response(serializer.data)

