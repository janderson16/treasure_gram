from django.shortcuts import render
from .models import Treasure
# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})

#
# class Treasure:
#     def __init__(self, name, value, material, location):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = location
#
# treasures = [
#     Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM"),
#     Treasure(name="Fool's Gold", value=0.00, material='pyrite', location="Fool's Falls, CO"),
#     Treasure(name='Coffee Can', value=20.00, material='tin', location="Acme, CA")
# ]
