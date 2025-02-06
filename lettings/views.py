import logging

import sentry_sdk
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Letting

logger = logging.getLogger(__name__)


def lettings_index(request):
    """
    View function to display a list of all lettings.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page displaying the list of lettings.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {"lettings_list": lettings_list}
        return render(request, "lettings/lettings_index.html", context)
    except Exception as e:
        logger.error("Error fetching lettings", exc_info=True)
        sentry_sdk.capture_exception(e)
        raise  # 500


def letting(request, letting_id):
    """
    View function to display details of a specific letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: Rendered HTML page displaying the letting details.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            "title": letting.title,
            "address": letting.address,
        }
        return render(request, "lettings/letting.html", context)
    except Http404:
        logger.warning(f"Letting {letting_id} not found (404)")
        raise  # 404
    except Exception as e:
        logger.error(f"Error displaying letting {letting_id}", exc_info=True)
        sentry_sdk.capture_exception(e)
        raise  # 500
