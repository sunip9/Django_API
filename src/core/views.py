from django.http import JsonResponse

from django.shortcuts import render


def test_view(request):
    data = {
        'name': 'Sunip',
        'age': 30
    }
    return JsonResponse(data)
