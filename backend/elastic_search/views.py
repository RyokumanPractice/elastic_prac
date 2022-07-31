from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Category
from .documents import CategoryDocument


@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'GET':
        return test_get(request)
    if request.method == 'POST':
        return test_post(request)


def test_get(request):
    search_value = request.GET.get('value')
    search_result = CategoryDocument.search().filter("term", name=search_value)
    return_result = []
    num = 1
    for hit in search_result:
        return_result.append(dict({'number': num, 'name': hit.name, 'desc': hit.desc}))
    return JsonResponse({'result': return_result}, status=200)


def test_post(request):
    name = request.data['name']
    desc = request.data['desc']
    category = Category(
        name=name,
        desc=desc
    )
    category.save()
    return JsonResponse({'message': str(category)}, status=201)
