from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Post


class IndexAPIView(APIView):
    def get(self, request):
        return Response({"ok": 'get', 'data': [1, 2, 3]})

    def post(self, request):
        return Response({"ok": 'post'})

    def delete(self, request):
        return Response({"ok": 'delete'})


def index(request):
    response = []
    for cat in Category.objects.order_by("-id").all():
        response.append({
            "id": cat.id,
            "name": cat.name,
            "image": cat.image.url
        })
    return JsonResponse({"categories": response})


def posts(request, pk):
    paginator = Paginator(Post.objects.filter(category_id=pk).order_by("-pk").all(), 9)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    response = []
    for p in page.object_list:
        response.append({
            "id": p.id,
            "subject": p.subject,
            "content": p.content,
            "added_at": p.added_at
        })
    return JsonResponse(
        {
            "posts": response,
            "total_items": paginator.count
        }
    )
