from django.db import models

class Query(models.Model):
    phrase = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

    class Meta:
        unique_together = ('phrase', 'region')


class Counter(models.Model):
    query = models.ForeignKey(Query, related_name='counters', on_delete=models.CASCADE)
    count = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
