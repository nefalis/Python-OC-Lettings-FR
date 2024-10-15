from django.shortcuts import render


def index(request):
    """
    View function to render the index page.
    """
    return render(request, 'index.html')
