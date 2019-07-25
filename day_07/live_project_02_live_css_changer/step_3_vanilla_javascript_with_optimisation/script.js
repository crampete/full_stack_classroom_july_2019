function handleCSSChange(elem) {
  console.log(elem);
  console.log(elem.name);

  var targetDiv = document.getElementById("target");

  // getting the CSS properties
  var cssAttrib = elem.name;
  var cssValue = elem.value;

  // changing the CSS of the target div
  targetDiv.style.setProperty(cssAttrib, cssValue);
}
