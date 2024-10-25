import logging
from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    View function to render the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View function to render a specific user profile.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        logger.error(f"Error retrieving profile for user {username}: {e}")
        return render(request, '404.html', status=404)
