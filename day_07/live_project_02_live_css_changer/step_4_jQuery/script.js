function handleCSSChange(elem) {
  var jQueryWrapped = $(elem);

  var targetDiv = $("#target");

  // Getting the respective values
  var cssProperty = jQueryWrapped.attr("name");
  var cssValue = jQueryWrapped.val();

  // changing the CSS value of the respective div
  targetDiv.css(cssProperty, cssValue);

  // or if you want to do it in one line
  // targetDiv.css($(elem).attr("name"), $(elem).val());
}
