from django.shortcuts import render
from django.templatetags.static import static

from presentations.models import Presentation

TEMPLATES = {
    Presentation.PresentationType.PDF: "screens/main-screen-pdf.html",
    Presentation.PresentationType.EMBED: "screens/main-screen-embed.html",
}

# Create your views here.
def index(request, presentation_id, page=1):
    presentation = Presentation.objects.get(id=presentation_id)
    context = {
        "page": page,
        "presentation": presentation,
    }
    return render(request, TEMPLATES[presentation.type], context)


def test_drive(request):
    return render(request, "screens/test-drive.html")
