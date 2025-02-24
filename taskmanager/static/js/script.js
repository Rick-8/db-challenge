// Sidenav Initialization with options
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var options = {
      edge: 'left', // Side from which the sidenav will open
      draggable: true // Enable dragging to close the sidenav
  };
  M.Sidenav.init(elems, options);
});

