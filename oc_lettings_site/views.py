from django.shortcuts import render


def index(request):
    return render(request, "index.html")


# Personalized view for error 404
def custom_404_view(request, exception):
    return render(request, "404.html", status=404)


# Personalized view for error 500
def custom_500_view(request):
    return render(request, "500.html", status=500)
