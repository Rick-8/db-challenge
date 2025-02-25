 // Sidenav Initialization with options
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".sidenav");
  var options = {
    edge: "left", // Side from which the sidenav will open
    draggable: true, // Enable dragging to close the sidenav
  };
  M.Sidenav.init(elems, options);


  // Datepicker initialization
  var datepicker = document.querySelectorAll(".datepicker");
  M.Datepicker.init(datepicker, {
  format: "yyyy-mm-dd",
  i18n: {
    done: "Select"
  }
  });

  // select initialization
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);

  // collapsible initialization
  var collapsibles = document.querySelectorAll('.collapsible');
  var instances = M.Collapsible.init(collapsibles);

});
