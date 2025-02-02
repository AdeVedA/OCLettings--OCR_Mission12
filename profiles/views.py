from django.shortcuts import get_object_or_404, render

from .models import Profile


def profiles_index(request):
    """
    Handle the request to display the list of profiles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying all profiles.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/profiles_index.html", context)


def profile(request, username):
    """
    Handle the request to display a specific profile by username.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is being requested.

    Returns:
        HttpResponse: The rendered HTML page displaying the user's profile.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
