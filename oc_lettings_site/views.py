from django.shortcuts import render


def index(request):
    """
    View function to render the index page.
    """
    return render(request, 'index.html')


def handler_404(request, exception):
    return render(request, "404.html", status=404)


def handler_500(request, exception):
    return render(request, "500.html", status=500)
