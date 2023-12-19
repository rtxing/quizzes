from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.db import connection

def get_quizzes(request, shop):
	"""Gets quizzes linked to a store.

    Parameters
    ----------
    values : Store ID

    Returns
    -------
    result : List of quiz ID's
       
    """
	cursor = connection.cursor()
	query = '''select quizzes.id from shops, quizzes
				where shops.id= quizzes.shop and shops.id = ''' + str(shop)
	cursor.execute(query)
	rows = cursor.fetchall()
	cursor.close()
	return JsonResponse({'quizzes':rows})