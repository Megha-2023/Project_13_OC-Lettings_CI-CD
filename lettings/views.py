from django.shortcuts import render
from .models import Letting


# Create your views here.
def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'letting_index.html', context)


def letting(request, letting_id):
    letting_obj = Letting.objects.get(id=letting_id)
    context = {
        'title': letting_obj.title,
        'address': letting_obj.address,
    }
    return render(request, 'letting.html', context)
