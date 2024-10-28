import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
    View function to render the index page.
    """
    return render(request, 'index.html')


def handler_404(request, exception):
    """
    Custom handler for 404 errors.
    """
    logger.warning(f"404 Error: {request.path} not found.")
    return render(request, "404.html", status=404)


def handler_500(request, exception):
    """
    Custom handler for 500 errors.
    """
    logger.error(f"500 Error occurred on {request.path}.")
    return render(request, "500.html", status=500)
