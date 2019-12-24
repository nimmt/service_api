import uuid
from django.shortcuts import render
from django.http.response import JsonResponse

from tables.models import Table

def create(request):
    table = Table(id=uuid.uuid4())

    table.save()

    return JsonResponse({'id': table.id}, status=201)
