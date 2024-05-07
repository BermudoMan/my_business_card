$('a').click(function() {
  switch ($(this).text()) {
  case "L":
    $('.Scroll').scrollLeft(-300);
    break;

  case "R":
    $('.Scroll').scrollLeft(300);
    break;
  }
});