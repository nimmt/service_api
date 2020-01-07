import uuid
import json
from django.core.cache import cache
from django.shortcuts import render
from django.http.response import JsonResponse

from tables.models import Table, Player

def create(request):
    table = Table(id=uuid.uuid4())

    table.save()

    return JsonResponse({'id': table.id}, status=201)

def show(request, tableId):
    table = Table.objects.get(id=tableId)

    players = Player.objects.filter(table=table)

    return JsonResponse({
      'id': table.id,
      'players': [{'id': player.id, 'name': player.name} for player in players]
    })

def create_player(request, tableId):
    table = Table.objects.get(id=tableId)

    body = json.loads(request.body)

    player = Player(id=str(uuid.uuid4()), table=table, name=body['name'])

    player.save()

    access_token = str(uuid.uuid4())

    cache.set(
      '/tables/{}/player_sessions/{}'.format(tableId, access_token),
      player,
      timeout = 24*60*60
    )

    return JsonResponse({'accessToken': access_token}, status=201)

def player_session(request, tableId):
    scheme, access_token = request.META.get('HTTP_AUTHORIZATION').split(' ')

    player = cache.get('/tables/{}/player_sessions/{}'.format(tableId, access_token))

    if not player:
        return JsonResponse({'message': 'Unauthorized'}, status=401)

    return JsonResponse({'id': player.id, 'name': player.name})
