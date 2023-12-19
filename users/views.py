from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.db import connection

def my_custom_sql(request, shop):
	cursor = connection.cursor()
	query = '''select shops.id,shops.shopname, quizzes.id, quizzes.question from shops, quizzes
				where shops.id= quizzes.shop and shops.id = ''' + str(shop)
	cursor.execute(query)
	rows = cursor.fetchall()
	cursor.close()
	return JsonResponse({'result':rows})