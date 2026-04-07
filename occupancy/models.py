#from django.db import models

# Create your models here.
from django.db import models

class OccupancyRecord(models.Model):

    room_name = models.CharField(max_length=100)
    people_count = models.IntegerField()
    capacity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_name} - {self.people_count}"