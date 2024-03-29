<script src="//mozilla.github.io/pdf.js/build/pdf.js"></script>
<script>
  // If absolute URL from the remote server is provided, configure the CORS
  // header on that server.
  var url = "/{{ presentation.pdf_file.name }}";

  // Loaded via <script> tag, create shortcut to access PDF.js exports.
  var pdfjsLib = window['pdfjs-dist/build/pdf'];

  // The workerSrc property shall be specified.
  pdfjsLib.GlobalWorkerOptions.workerSrc = '//mozilla.github.io/pdf.js/build/pdf.worker.js';

  // Asynchronous download of PDF
  var loadingTask = pdfjsLib.getDocument(url);
  loadingTask.promise.then(function(pdf) {
    console.log('PDF loaded');
    var currentPageNumber = 0;
    async function display_pdf(){
      // Fetch the first page
      const requestPageNumber = await fetch("{% url 'get-slot-page' %}?slot_id={{slot.id}}");
      const pageNumber = (await requestPageNumber.json())["current_page"];
      if (pageNumber === currentPageNumber) return;
      currentPageNumber = pageNumber;
      console.log(pageNumber)
      pdf.getPage(pageNumber).then(function(page) {
        console.log('Page loaded');
        
        var scale = 4;
        var viewport = page.getViewport({scale: scale});

        // Prepare canvas using PDF page dimensions
        var canvas = document.getElementById('the-canvas');
        var context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        // Render PDF page into canvas context
        var renderContext = {
          canvasContext: context,
          // Transparent background so that it doesn't flash white while loading
          background: 'rgba(0,0,0,0)',
          viewport: viewport
        };
        var renderTask = page.render(renderContext);
        renderTask.promise.then(function () {
          console.log("New page loaded");
        });
      });
    }
    {% comment %} setInterval(display_pdf, 100); {% endcomment %}
    {% comment %} display_pdf() {% endcomment %}
  }, function (reason) {
    // PDF loading error
    console.error(reason);
  });
</script>