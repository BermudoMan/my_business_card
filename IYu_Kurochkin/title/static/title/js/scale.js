setZoom();
window.addEventListener('resize', setZoom);

function setZoom() {
  if (window.matchMedia('(min-width: 780px) and (max-width: 1380px)').matches) {
    document.body.style.zoom = "70%";
  } else {
    document.body.style.zoom = "100%";
  }
}