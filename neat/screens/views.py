from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request, page):
    return render(request, "screens/main-screen.html", {"page": page})


def test_drive(request):
    return render(request, "screens/test-drive.html")
