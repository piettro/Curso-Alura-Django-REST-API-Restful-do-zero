from django.http import JsonResponse
from django.shortcuts import render

def students(request):

    if request.method == 'GET':
        data = {
            'students': [
                {'id': 1, 'name': 'Alice', 'age': 20},
                {'id': 2, 'name': 'Bob', 'age': 22},
                {'id': 3, 'name': 'Charlie', 'age': 21},
            ]
        }
        return JsonResponse(data)
