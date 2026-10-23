function renderDiagrams() {
  document.querySelectorAll('.acquisition-diagram').forEach(function(container) {
    if (typeof window.parseProtocolFromDOM === 'function' && typeof window.renderAcquisitionDiagram === 'function') {
      const data = window.parseProtocolFromDOM(document);
      window.renderAcquisitionDiagram(container, data);
    }
  });
}

// Run immediately — scripts load at end of <body>, so DOM is fully parsed here.
renderDiagrams();

// Also hook into MkDocs Material SPA navigation for instant-loading mode.
if (typeof document$ !== 'undefined') {
  document$.subscribe(renderDiagrams);
}
