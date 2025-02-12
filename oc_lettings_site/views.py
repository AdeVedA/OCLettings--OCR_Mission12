from django.shortcuts import render


def index(request):
    """
    View function to display the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page for the index.
    """
    return render(request, "index.html")


# Personalized view for error 404
def custom_404_view(request, exception):
    """
    Custom view for handling 404 errors.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404.

    Returns:
        HttpResponse: Rendered 404 error page.
    """
    return render(request, "404.html", status=404)


def custom_500_view(request):
    """
    Custom view for handling 500 errors.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 500 error page.
    """
    return render(request, "500.html", status=500)
