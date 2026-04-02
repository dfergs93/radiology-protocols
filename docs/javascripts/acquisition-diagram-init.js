document$.subscribe(function() {
  const diagrams = document.querySelectorAll('.acquisition-diagram');
  diagrams.forEach(function(container) {
    if (typeof window.parseProtocolFromDOM === 'function' && typeof window.renderAcquisitionDiagram === 'function') {
      const data = window.parseProtocolFromDOM(document);
      window.renderAcquisitionDiagram(container, data);
    }
  });
});
