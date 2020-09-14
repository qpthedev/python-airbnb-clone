from django.views.generic import ListView, DetailView
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