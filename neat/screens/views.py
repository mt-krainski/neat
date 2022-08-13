from django.http import Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from screens.models import PresentationSlot

from presentations.models import Presentation


def _get_slot_by_slot_id(slot_id):
    if not slot_id:
        raise Http404("Missing slot parameter!")

    try:
        slot = PresentationSlot.objects.get(id=slot_id)
    except PresentationSlot.DoesNotExist:
        raise Http404("Presentation slot not found!")

    return slot


def main_screen(request):
    # TODO: make this more formal. For now we assume that there's only active slot
    try:
        slot = PresentationSlot.objects.get(active=True)
    except PresentationSlot.DoesNotExist:
        return render(request, "screens/no-active-presentation.html")
    presentation = slot.presentation
    context = {
        "slot": slot,
        "presentation": presentation,
        "presentation_type": presentation.get_type_display(),
    }
    return render(request, "screens/main-screen.html", context)


def presenter_screen(request, slot_id):
    slot = _get_slot_by_slot_id(slot_id)
    presentation = slot.presentation
    # TODO: make this more formal. For now we assume that there's only one slot
    #   per presentation
    slot = presentation.presentationslot_set.first()
    context = {
        "slot": slot,
        "presentation": presentation,
        "presentation_type": presentation.get_type_display(),
    }
    return render(request, "screens/presenter-screen.html", context)


def get_slot_page(request):
    slot = _get_slot_by_slot_id(request.GET.get("slot_id"))
    return JsonResponse({"current_page": slot.current_page})


def get_active_slot(request):
    active_slot = None
    try:
        slot = PresentationSlot.objects.get(active=True)
        active_slot = slot.id
    except (PresentationSlot.DoesNotExist, PresentationSlot.MultipleObjectsReturned):
        pass

    return JsonResponse({"active_slot": active_slot})
