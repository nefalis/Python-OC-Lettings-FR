import logging
from django.shortcuts import render, get_object_or_404
from .models import Letting


logger = logging.getLogger(__name__)


def index(request):
    """
    View function to display the index page of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View function to display details of a specific letting.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        logger.error(f"Error retrieving letting with id {letting_id}: {e}")
        return render(request, '404.html', status=404)
