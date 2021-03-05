from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TabletopSerializer, UsrSerializer

from .models import Tabletop, Usr

class TabletopViewSet(viewsets.ModelViewSet):
    queryset = Tabletop.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TabletopSerializer

class UsrViewSet(viewsets.ModelViewSet):
    queryset = Usr.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsrSerializer

@api_view(['GET', 'PUT'])
def subscribe(request, pk, format=None):
    try:
        table = Tabletop.objects.get(pk=pk)
    except Tabletop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        people = table.players
        return Response(people)
    
    if request.method == 'PUT':
        newTable = Tabletop.objects.get(pk=pk)
        users = request.data.get('users')
        users = [user['id'] for user in users]
        newTable.players.set(users)
        serializer = TabletopSerializer(table, data=newTable)
        if serializer.is_valid() :
            serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'PUT'])
def unsubscribe(request, pk, format=None):
    try:
        table = Tabletop.objects.get(pk=pk)
    except Tabletop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        allPeople = set(Usr.objects.all())
        unsubscribers = allPeople - {*table.players, table.owner}
        return Response(unsubscribers)
    
    if request.method == 'PUT':
        newTable = Tabletop.objects.get(pk=pk)
        users = request.data.get('users')
        users = set(user['id'] for user in users)
        users = newTable.players - users
        newTable.players.set(users)
        serializer = TabletopSerializer(table, data=newTable)
        if serializer.is_valid() :
            serializer.save()
        return Response(serializer.data)
