<script>
    const slot = {{ slot.id }};
    var currentPageNumber = 0;
    async function reloadPresentation(){
    console.log("Checking page...")
    const requestPageNumber = await fetch("{% url 'get-slot-page' %}?slot_id={{slot.id}}");
    const pageNumber = (await requestPageNumber.json())["current_page"];
    if (currentPageNumber === pageNumber) return;

    const presentationFrame = document.getElementById("presentation-frame");
    presentationFrame.src = "{{ presentation.embed_url }}?rm=minimal&slide=" + pageNumber;
    currentPageNumber = pageNumber;
    };

    setInterval(reloadPresentation, 500);
</script>