from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import Query, Counter
from .serializers import QuerySerializer


class AddView(CreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class StatView(APIView):

    def get(self, request):
        query_id = request.data.get('query_id')
        start_time = request.data.get('start_time')
        finish_time = request.data.get('finish_time')
        saved_query = get_object_or_404(Query.objects.all(), pk=query_id)
        counters = Counter.objects.filter(time__gt=start_time, time__lte=finish_time, query=query_id)
        count_timestamp = [[obj.count, obj.time] for obj in counters]
        return Response({
            "query": "{} in {}".format(saved_query.phrase, saved_query.region),
            "counters": count_timestamp
        })
