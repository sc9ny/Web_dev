window.onload = function() {
  var x = document.getElementsByTagName("a");
  for (var i =0; i < x.length; i++){
    if (document.URL == x[i].href) {
      x[i].className = "current";
    }
  }
};
