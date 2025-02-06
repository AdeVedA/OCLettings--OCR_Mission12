import logging

import sentry_sdk
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """
    View function to display the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page for the index.
    """
    try:
        return render(request, "index.html")
    except Exception as e:
        logger.error("Error displaying the home page", exc_info=True)
        sentry_sdk.capture_exception(e)
        raise  # 500


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
    logger.warning(f"Page not found : {request.path}")
    return render(request, "404.html", status=404)


def custom_500_view(request):
    """
    Custom view for handling 500 errors.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered 500 error page.
    """
    logger.error("500 server error detected", exc_info=True)
    return render(request, "500.html", status=500)
