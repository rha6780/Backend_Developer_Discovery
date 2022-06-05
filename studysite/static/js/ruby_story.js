function resizeApply() {
    var minWidth = 1000;
    var body = document.getElementsByTagName('body')[0];
    if (window.innerWidth < minWidth) { body.style.zoom = (window.innerWidth / minWidth); }
    else body.style.zoom = 1;
  }
  
  window.onload = function() {
    window.addEventListener('resize', function() {
      resizeApply();
    });
  }
  
  resizeApply();


