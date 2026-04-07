from django.shortcuts import render
from .models import OccupancyRecord
from .ai.detect_people import detect_people


def dashboard(request):

    records = OccupancyRecord.objects.all().order_by('-timestamp')[:10]

    return render(
        request,
        "occupancy/dashboard.html",
        {"records": records}
    )


def detect(request):

    people_count = detect_people()

    room = "Main Hall"
    capacity = 100

    if people_count == 0:
        suggestion = "Room Empty → Turn OFF Lights and AC"

    elif people_count < capacity * 0.2:
        suggestion = "Room Underutilized → Suggest Smaller Room"

    elif people_count > capacity * 0.9:
        suggestion = "Room Almost Full → Capacity Warning"

    else:
        suggestion = "Room Usage Optimal"

    OccupancyRecord.objects.create(
        room_name=room,
        people_count=people_count,
        capacity=capacity
    )

    records = OccupancyRecord.objects.all().order_by('-timestamp')[:10]

    return render(
        request,
        "occupancy/dashboard.html",
        {
            "people": people_count,
            "records": records,
            "suggestion": suggestion
        }
    )