# from django.shortcuts import render
# from django.http import HttpResponse, Http404
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

@api_view(['GET', 'PUT'])
def subscribe(request, pk, format=None):
    try:
        table = Tabletop.objects.get(pk=pk)
    except Tabletop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        tmp = UsrSerializer(table.owner)
        return Response(tmp.data)

#   @Put(':id/sub')
#   subscribe(@Param('id') tableId: number, @Body() users: IUsr[]) {
#     this.tableService.subscribeUsers(tableId, users);
#     return this.tableService.getSubscribersAndNotsub(tableId);
#   }

#   @Get(':id/sub')
#   getSubscribers(@Param('id') tableId: number) {
#     return this.tableService.getSubscribers(tableId);
#   }

#   @Put(':id/unsub')
#   unsubscribe(@Param('id') tableId: number, @Body() users: IUsr[]) {
#     this.tableService.unSubscribeUsers(tableId, users);
#     return this.tableService.getSubscribersAndNotsub(tableId);    
#   }

#   @Get(':id/unsub')
#   getUnSubscribers(@Param('id') tableId: number) {
#     return this.tableService.getAllUnSubscribers(tableId);
#   }