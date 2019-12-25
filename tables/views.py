import uuid
import json
from django.shortcuts import render
from django.http.response import JsonResponse

from tables.models import Table, Player

def create(request):
    table = Table(id=uuid.uuid4())

    table.save()

    return JsonResponse({'id': table.id}, status=201)

def create_player(request, tableId):
    table = Table.objects.get(id=tableId)

    body = json.loads(request.body)

    player = Player(id=uuid.uuid4(), table=table, name=body['name'])

    player.save()

    return JsonResponse({'id': player.id, 'name': player.name})
