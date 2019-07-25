// gets executed only when the
// DOM is ready
(function() {
  // not necessary but helps enhance
  // stability. Dont' worry too much about this
  "use strict";

//   var addHeading = function() {
  function addHeading() {
    var newDivToAdd = document.createElement("div");
    // adding relevant CSS class to the div
    newDivToAdd.classList.add("addable");

    var newHeaderToAdd = document.createElement("h3");
    var textContent = document.createTextNode("Text added dynamically");

    // adding text to the heading tag
    newHeaderToAdd.appendChild(textContent);
    // adding the heading to the div tag
    newDivToAdd.appendChild(newHeaderToAdd);

    // adding div to the body. This step makes is visible in the DOM
    document.getElementById("add-target").appendChild(newDivToAdd);
  };

  // attaching a listener on the button that activates the above
  // function when clicked
  document.getElementById("add-button").addEventListener("click", addHeading);
})();
