from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse


def check(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM auth_user WHERE is_superuser = 1")
        superuser_count = cursor.fetchone()[0]
        if superuser_count > 0:
            return HttpResponse("В базе данных есть суперпользователи")
        else:
            return HttpResponse("В базе данных нет суперпользователей")
