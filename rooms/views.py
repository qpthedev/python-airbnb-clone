from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


# Create your views here.
class HomeView(ListView):
    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    parginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    """ RoomDetail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "US")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    instant = request.GET.get("super_host", False)
    super_host = request.GET.get("instant", False)
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "super_host": super_host,
        "instant": instant,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
    }

    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
