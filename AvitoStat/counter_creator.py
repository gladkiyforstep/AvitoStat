from .WebHelper import WebHelper
from .models import Query, Counter


def create_counters():
    queries = Query.objects.all()
    for q in queries:
        counter = Counter()
        req = WebHelper(q.phrase, q.region)
        counter.count = req.get_count()
        counter.query = q
        counter.save()
    print('counters are saved')