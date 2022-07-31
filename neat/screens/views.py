from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from screens.models import PresentationSlot

from presentations.models import Presentation

TEMPLATES = {
    Presentation.PresentationType.PDF: "screens/main-screen-pdf.html",
    Presentation.PresentationType.EMBED: "screens/main-screen-embed.html",
}

# Create your views here.
def index(request, presentation_id):
    presentation = Presentation.objects.get(id=presentation_id)
    # TODO: make this more formal. For now we assume that there's only one slot
    #   per presentation
    slot = presentation.presentationslot_set.first()
    context = {
        "slot": slot,
        "presentation": presentation,
        "presentation_type": presentation.get_type_display(),
    }
    return render(request, "screens/main-screen.html", context)


def get_slot_page(request):
    slot_id = request.GET.get("slot_id")

    if not slot_id:
        return HttpResponseNotFound("Missing slot parameter!")

    try:
        slot = PresentationSlot.objects.get(id=slot_id)
    except PresentationSlot.DoesNotExist:
        return HttpResponseNotFound("Presentation slot not found!")

    return JsonResponse({"current_page": slot.current_page})
