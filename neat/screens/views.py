from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.shortcuts import render

from screens.models import PresentationSlot


def _get_slot_by_slot_id(slot_id):
    """Get slot by ID for the purpose of views.

    Raises Http exceptions for various cases.

    Args:
        slot_id (int): id of the slot you want to get

    Raises:
        HttpResponseBadRequest: if the slot_id is None or empty
        HttpResponseNotFound: if the slot with that id doesn't exist

    Returns:
        PresentationSlot: presentation slot with the given id
    """
    if not slot_id:
        raise HttpResponseBadRequest("Missing slot parameter!")

    try:
        slot = PresentationSlot.objects.get(id=slot_id)
    except PresentationSlot.DoesNotExist:
        raise HttpResponseNotFound("Presentation slot not found!")

    return slot


def main_screen(request):
    """Render main screen."""
    try:
        slot = PresentationSlot.objects.get(active=True)
    except (PresentationSlot.DoesNotExist, PresentationSlot.MultipleObjectsReturned):
        return render(request, "screens/no-active-presentation.html")
    presentation = slot.presentation
    context = {
        "slot": slot,
        "presentation": presentation,
        "presentation_type": presentation.get_type_display(),
    }
    return render(request, "screens/main-screen.html", context)


def presenter_screen(request, slot_id):
    """Render presenter screen for a given slot id."""
    slot = _get_slot_by_slot_id(slot_id)
    presentation = slot.presentation
    context = {
        "slot": slot,
        "presentation": presentation,
        "presentation_type": presentation.get_type_display(),
    }
    return render(request, "screens/presenter-screen.html", context)


def get_slot_page(request):
    """Return the current page for a given slot."""
    slot = _get_slot_by_slot_id(request.GET.get("slot_id"))
    return JsonResponse({"current_page": slot.current_page})


def get_active_slot(request):
    """Return the id of the currently active slot."""
    active_slot = None
    try:
        slot = PresentationSlot.objects.get(active=True)
        active_slot = slot.id
    except (PresentationSlot.DoesNotExist, PresentationSlot.MultipleObjectsReturned):
        pass

    return JsonResponse({"active_slot": active_slot})
