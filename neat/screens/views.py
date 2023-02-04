from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from screens.models import PresentationSlot


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
    slot = get_object_or_404(PresentationSlot, id=slot_id)
    presentation = slot.presentation
    context = {
        "slot": slot,
        "presentation": presentation,
        "presentation_type": presentation.get_type_display(),
    }
    return render(request, "screens/presenter-screen.html", context)


def get_slot_page(request):
    """Return the current page for a given slot."""
    slot = get_object_or_404(PresentationSlot, id=request.GET.get("slot_id"))
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


def next_slide(request):
    print("Next slide triggered.")
    return ""
